from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_path", default="C:\drivers")
    parser.addoption("--url", default="https://www.google.com/")


@pytest.fixture
def base_url(request):
    return request.config.getoption(f"--url")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_path = request.config.getoption("--driver_path")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f"{driver_path}\chromedriver")
    else:
        raise ValueError("don't find this driver..")

    def fin():
        browser.quit()

    request.addfinalizer(fin)
    browser.maximize_window()
    return browser
