from pages.widgets.progressbar import ProgressBarPage

def test_progressbar(driver):
    progress_page = ProgressBarPage(driver)
    progress_page.open()

    progress_page.start_progress()
    progress_page.wait_until_complete()

    final_value = progress_page.get_progress_value()
    assert final_value == "100%", f"Expected 100%, but got {final_value}"
