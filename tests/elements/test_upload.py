import os
import requests
from pages.elements.upload import UploadDownloadPage

def test_upload_file(driver):
    upload_page = UploadDownloadPage(driver)
    upload_page.open()

    # Create a temp file for upload testing
    test_file = os.path.abspath("test_upload.txt")
    with open(test_file, "w") as f:
        f.write("DemoQA upload test file.")

    upload_page.upload_file(test_file)
    uploaded_name = upload_page.get_uploaded_file_name()

    print(f"Uploaded File Name: {uploaded_name}")
    assert uploaded_name == "test_upload.txt"

    os.remove(test_file)

def test_download_file(driver):
    download_page = UploadDownloadPage(driver)
    download_page.open()
    download_href =  download_page.get_download_link()
    print(f"Download HREF: {download_href[:50]}...")

    # Check that it's a valid data URL
    assert download_href.startswith("data:image/jpeg;base64,"), "Download link is not a valid base64 image."
