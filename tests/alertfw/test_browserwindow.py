from pages.alertfw.browserwindow import BrowserWindowPage

def test_browserwindow(driver):
    browser_page = BrowserWindowPage(driver)
    browser_page.open()

    browser_page.open_new_tab()
    browser_page.open_new_window()