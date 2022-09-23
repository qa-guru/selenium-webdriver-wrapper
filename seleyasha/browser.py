from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from seleyasha.selector import to_locator
from seleyasha.wait import WebDriverWait


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, timeout=2, ignored_exceptions=(WebDriverException,)
        )

    def assert_(self, condition):
        return self.wait.until(condition)

    def open(self, url):
        self.driver.get(url)

    def back(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()

    def element(self, selector):
        def find_visible(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            if not webelement.is_displayed():
                raise AssertionError(
                    f'element is not displayed: {webelement.get_attribute("outerHTML")}'
                )
            return webelement

        return self.wait.until(
            find_visible, message=f'element by {selector} is not ready'
        )

    def type(self, selector, value):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.send_keys(value)
            return webelement

        return self.wait.until(
            command, message=f'failed to type «{value}» into element by {selector}'
        )

    def click(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = driver.find_element(*to_locator(selector))
            webelement.click()
            return webelement

        return self.wait.until(
            command, message=f'failed to click on element by {selector}'
        )
