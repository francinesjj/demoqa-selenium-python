from pages.alertfw.alert import AlertPage

def test_alert(driver):
    alert_page = AlertPage(driver)
    alert_page.open()

    alert_page.click_alert_btn()
    alert_page.click_time_alert()
    alert_page.click_confirm_alert()
    alert_page.click_cancel_alert()