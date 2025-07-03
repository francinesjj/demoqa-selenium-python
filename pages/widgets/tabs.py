from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TabsPage:
    def __init__(self, driver):
        self.driver = driver
        self.tabs = {
            "What": (By.ID, "demo-tab-what"),
            "Origin": (By.ID, "demo-tab-origin"),
            "Use": (By.ID, "demo-tab-use"),
            "More": (By.ID, "demo-tab-more")
        }
        self.contents = {
            "What": (By.ID, "demo-tabpane-what"),
            "Origin": (By.ID, "demo-tabpane-origin"),
            "Use": (By.ID, "demo-tabpane-use"),
            "More": (By.ID, "demo-tabpane-more")
        }

    def open(self):
        self.driver.get("https://demoqa.com/tabs")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.tabs["What"])
        )

    def click_tab(self, tab_name):
        tab = self.driver.find_element(*self.tabs[tab_name])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tab)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tabs[tab_name]))

        # js click
        self.driver.execute_script("arguments[0].click();", tab)

    def get_tab_content(self, tab_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.contents[tab_name])
        )
        return self.driver.find_element(*self.contents[tab_name]).text.strip()
