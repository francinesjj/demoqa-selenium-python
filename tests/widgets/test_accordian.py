from pages.widgets.accordian import AccordianPage

def test_accordian(driver):
    accordian_page = AccordianPage(driver)
    accordian_page.open()
    accordian_page.click_accordion()