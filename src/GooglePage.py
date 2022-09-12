import time

from selenium.webdriver import Keys

from src.BasePage import BasePage
from src.GooglePageLocators import GooglePageLocators
import pytest_check as check


class GooglePage(BasePage):
    PRODUCT_NAME = "Think24.ru"
    CURRENT_PRODUCT_URL = 'https://think24.center/'

    def open_google_page(self, base_url):
        self.driver.get(base_url)
        check.is_true(GooglePageLocators.GOOGLE_LOGO, "This is no google page!")

    def find_google_input_place(self, locator=GooglePageLocators
                                .SEARCH_PLACE, text=PRODUCT_NAME):
        element = self.find_and_input_text(locator=locator, text=text)
        element.send_keys(Keys.ENTER)
        input_google = self.find_element(GooglePageLocators.SEARCH_PLACE)
        check.equal(text, input_google.get_attribute('value'), "Wrong text in input place!")
        check.is_true(self.find_element(GooglePageLocators.THINK24_LINK), 'Link is not present in search resul!')

    def go_to_link_think24(self):
        self.click_of_element(locator=GooglePageLocators.THINK24_LINK)
        check.is_in(self.CURRENT_PRODUCT_URL, self.driver.current_url, "Incorrect url!")
