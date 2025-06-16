import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserWindowPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_tab_btn = (By.XPATH, "//div[@id='tabButtonWrapper']//button[@id='tabButton']")
        self.new_window_btn = (By.XPATH, "//div[@id='windowButtonWrapper']//button[@id='windowButton']")
        self.new_message_btn = (By.XPATH, "//div[@id='msgWindowButtonWrapper']//button[@id='messageWindowButton']")

    def open(self):
        self.driver.get("https://demoqa.com/browser-windows")
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

    def open_new_tab(self):
        original_window = self.driver.current_window_handle
        existing_windows = self.driver.window_handles

        new_tab = self.driver.find_element(*self.new_tab_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_tab)
        new_tab.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(existing_windows)
        )

        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)

        # wait until element is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # assert text is in the page
        page_text = self.driver.find_element(By.TAG_NAME, "h1").text
        assert "This is a sample page" in page_text, "Expected text not found in new tab"

        self.driver.close()
        self.driver.switch_to.window(original_window)

    def open_new_window(self):
        original_window = self.driver.current_window_handle
        existing_windows = self.driver.window_handles

        new_tab = self.driver.find_element(*self.new_window_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_tab)
        new_tab.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(existing_windows)
        )

        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)

        # wait until element is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # assert text is in the page
        page_text = self.driver.find_element(By.TAG_NAME, "h1").text
        assert "This is a sample page" in page_text, "Expected text not found in new tab"

        self.driver.close()
        self.driver.switch_to.window(original_window)

    def open_new_message(self):
        original_window = self.driver.current_window_handle
        existing_windows = self.driver.window_handles

        new_tab = self.driver.find_element(*self.new_message_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_tab)
        new_tab.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(existing_windows)
        )

        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)

        # wait until element is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # assert text is in the page
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization." in page_text, "Expected text not found in new tab"

        self.driver.close()
        self.driver.switch_to.window(original_window)