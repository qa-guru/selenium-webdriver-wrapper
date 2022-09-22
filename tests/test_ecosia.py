from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

from seleyasha.shared import assert_that
from seleyasha.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.conditions import number_of_elements
from seleyasha.commands import type, click
from seleyasha import shared

shared.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
shared.wait = WebDriverWait(shared.driver, timeout=2, ignored_exceptions=(WebDriverException,))

# 2
# browser = Browser(driver)

shared.driver.get('https://ecosia.org')
# 2
# browser.open('https://ecosia.org')

'''
# in Selene:
browser.element('[name=q]').type('selene').press_enter()
# in Selenium WebDriver:
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)
# OR with wait
def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name=q]')
wait.until(find_element).send_keys('selene', Keys.ENTER)
# OR with built-in expected condition
wait.until(visibility_of_element_located((By.NAME, 'q'))).send_keys('selene yashaka', Keys.ENTER)
# OR with custom expected condition
wait.until(element('[name=q]')).send_keys('selene yashaka', Keys.ENTER)
'''

query = '[name=q]'
type(query, value='selene' + Keys.ENTER)
# 2
# browser.type('[name=q]', value='selene' + Keys.ENTER)
# 3
# element('[name=q]').type('selene' + Keys.ENTER)
# ...
# query = element('[name=q]')
# query.type('selene' + Keys.ENTER)

shared.driver.back()

type(query, value=' github issues' + Keys.ENTER)
# 2
# browser.type(query, ' yashaka' + Keys.ENTER)
# 3
# query.type(' yashaka' + Keys.ENTER)

click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
# 2
# browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=25))
# 2
# browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
'''
# less stable version:
number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 4
'''

shared.driver.quit()
