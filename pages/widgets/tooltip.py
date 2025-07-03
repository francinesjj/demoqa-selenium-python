from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ToolTipPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/tool-tips"
        self.button = (By.ID, "toolTipButton")
        self.tooltip_text = (By.CLASS_NAME, "tooltip-inner")

    def open(self):
        self.driver.get(self.url)

    def hover_and_get_tooltip(self, element_locator):
        element = self.driver.find_element(*element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # Wait for tooltip to appear
        self.driver.implicitly_wait(2)

        tooltip = self.driver.find_element(*self.tooltip_text)
        return tooltip.text