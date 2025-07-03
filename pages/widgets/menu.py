from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/menu"
        self.main_item_2 = (By.XPATH, "//a[text()='Main Item 2']")
        self.sub_sub_list = (By.XPATH, "//a[text()='SUB SUB LIST »']")
        self.sub_sub_item_1 = (By.XPATH, "//a[text()='Sub Sub Item 1']")

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)

    def hover_nested_menu(self):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        # Main Item 2
        main_item_2 = wait.until(EC.visibility_of_element_located(self.main_item_2))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", main_item_2)
        actions.move_to_element(main_item_2).perform()
        time.sleep(1.5)

        # SUB SUB LIST
        sub_sub_list = wait.until(EC.visibility_of_element_located(self.sub_sub_list))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sub_sub_list)
        actions.move_to_element(sub_sub_list).perform()
        time.sleep(1.5)

        # Sub Sub Item 1
        sub_sub_item_1 = wait.until(EC.visibility_of_element_located(self.sub_sub_item_1))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sub_sub_item_1)
        actions.move_to_element(sub_sub_item_1).perform()

        return sub_sub_item_1.is_displayed()
