from pages.alertfw.modals import ModalsPage

def test_modals(driver):
    modal_page = ModalsPage(driver)
    modal_page.open()

    modal_page.open_small_modal()
    modal_page.open_large_modal()