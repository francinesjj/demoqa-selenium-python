import requests
from pages.elements.brokenpage import BrokenPage

# check if images load or return 404 error
def test_image_links(driver):
    broken_page = BrokenPage(driver)
    broken_page.open()
    image_srcs = broken_page.get_image_sources()

    for src in image_srcs:
        response = requests.get(src)
        print(f"Checking Image: {src} → Status Code: {response.status_code}")
        assert response.status_code == 200 or response.status_code == 404

# checks if links are valid or broken according to status code
    link_urls = broken_page.get_link_urls()

    for url in link_urls:
        try:
            response = requests.get(url, timeout=5)
            print(f"Checking Link: {url} → Status Code: {response.status_code}")
            assert response.status_code in [200, 404, 500]
        except requests.exceptions.RequestException as e:
            print(f"Error checking {url}: {e}")
            assert False, f"Request failed for {url}"
