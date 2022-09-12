from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, base_url, wait=1):
        self.driver = driver
        self.url = base_url
        self.wait = WebDriverWait(driver, wait)

    def open_base_page(self, base_url):
        browser = self.driver.get(base_url)
        return browser

    def find_element(self, locator='locator'):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click_of_element(self, locator):
        actions = ActionChains(self.driver)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions.move_to_element(element).click().perform()
        return element

    def find_and_input_text(self, locator='locator', text='text'):
        actions = ActionChains(self.driver)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions.move_to_element(element).click().send_keys(text).perform()
        return element
