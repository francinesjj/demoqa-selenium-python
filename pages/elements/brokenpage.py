import time
from selenium.webdriver.common.by import By

class BrokenPage:
    def __init__(self, driver):
        self.driver = driver
        self.valid_image = (By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
        self.broken_image = (By.XPATH, "//img[@src='/images/Toolsqa_1.jpg']")

    def open(self):
        self.driver.get("https://demoqa.com/broken")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)

    def get_image_elements(self):
        # returns a list with 2 image elements (valid and broken img); locator tuple
        return [
            self.driver.find_element(*self.valid_image),
            self.driver.find_element(*self.broken_image)
        ]

    def get_image_sources(self):
        images = self.get_image_elements() # calls 1st method to get img and stores in img list
        return [img.get_attribute("src") for img in images] # extract img src and returns list of src url

    def get_link_elements(self):
        return self.driver.find_elements(By.TAG_NAME, "a") # finds a tags and href link

    def get_link_urls(self):
        links = self.get_link_elements() # calls get_links_elements
        return [link.get_attribute("href") for link in links if link.get_attribute("href") is not None] # gets href attributes and excludes a tags w/o href
