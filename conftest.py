import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Initialize the WebDriver
    driver.maximize_window()  # Optional: Maximize window
    yield driver  # Yield driver to the test
    driver.quit()  # Close the browser after the test
