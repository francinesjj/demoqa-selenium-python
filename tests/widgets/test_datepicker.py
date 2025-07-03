from pages.widgets.datepicker import DatepickerPage

def test_datepicker(driver):
    datepicker_page = DatepickerPage(driver)
    datepicker_page.open()

    datepicker_page.enter_date("11/05/2025")
    datepicker_page.enter_date_time("November 5, 2002 11:30 PM")