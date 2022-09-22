from selenium.webdriver.remote.webdriver import WebDriver
from seleyasha.wait import WebDriverWait

driver: WebDriver = ...
wait: WebDriverWait = ...


def assert_that(condition):
    return wait.until(condition)
