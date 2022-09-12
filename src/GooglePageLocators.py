from selenium.webdriver.common.by import By
from src.BasePage import BasePage


class GooglePageLocators(BasePage):
    SEARCH_PLACE = (By.CSS_SELECTOR, "input.gsfi")
    THINK24_LINK = (By.CSS_SELECTOR, "a[href='https://think24.center/']")
    GOOGLE_LOGO = (By.CSS_SELECTOR, "img[alt='Google']")
