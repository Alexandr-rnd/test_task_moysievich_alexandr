from src.GooglePage import GooglePage


def test_search_think24(driver, base_url):
    google_page = GooglePage(driver, base_url)
    google_page.open_google_page(base_url)
    google_page.find_google_input_place()
    google_page.go_to_link_think24()
