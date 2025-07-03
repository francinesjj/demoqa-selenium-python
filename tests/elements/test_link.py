import time
from pages.elements.link import LinkPage

def test_link(driver):
    link_page = LinkPage(driver)
    link_page.open()

    link_page.click_simple_link()
    link_page.click_dynamic_link()

    expected_responses = [
        (link_page.click_created, "201", "Created"),
        (link_page.click_no_content, "204", "No Content"),
        (link_page.click_moved, "301", "Moved Permanently"),  # ← this was the only mismatch
        (link_page.click_bad_request, "400", "Bad Request"),
        (link_page.click_unauthorized, "401", "Unauthorized"),
        (link_page.click_forbidden, "403", "Forbidden"),
        (link_page.click_not_found, "404", "Not Found"),
    ]

    for click_func, expected_code, expected_text in expected_responses:
        click_func() # runs the click functions above
        time.sleep(0.5)
        code, text = link_page.get_link_response() # grabs the text from the page and extracts it

        print("→ Parsed:", code, text) # shows extracted text (201 text Created)
        response_raw = link_page.driver.find_element(*link_page.link_response).text
        print("→ Raw text:", response_raw) # prints full unprocessed text for comparison

        assert code == expected_code, f"Expected {expected_code}, got {code}" # checks if the extracted status code matches the expected
        assert text.replace("text ", "") == expected_text, f"Expected '{expected_text}', got '{text}'" # removes the word "text"


