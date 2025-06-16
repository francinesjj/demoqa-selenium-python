import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadDownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.upload_input = (By.ID, "uploadFile")
        self.download_button = (By.ID, "downloadButton")
        self.uploaded_file_path = (By.ID, "uploadedFilePath")

    def open(self):
        self.driver.get("https://demoqa.com/upload-download")
        self.driver.maximize_window()
        time.sleep(1)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def upload_file(self, absolute_path):
        self.driver.find_element(*self.upload_input).send_keys(absolute_path)

    def get_uploaded_file_name(self):
        full_path = self.driver.find_element(*self.uploaded_file_path).text
        return os.path.basename(full_path)  # return just the filename

    def get_download_link(self):
        wait = WebDriverWait(self.driver, 10)
        download_link = wait.until(EC.element_to_be_clickable(self.download_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
        download_link.click()
        return download_link.get_attribute("href")


