from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.browser import Browser
from seleyasha.conditions import that

browser = Browser(
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
)

browser.open('https://ecosia.org')

query = '[name=q]'
browser.type(query, value='selene' + Keys.ENTER)
# 4
# browser.element('[name=q]').type('selene' + Keys.ENTER)
# ...
# query = element('[name=q]')
# query.type('selene' + Keys.ENTER)

browser.back()

browser.type(query, value=' github issues' + Keys.ENTER)
# 4
# query.type(' yashaka' + Keys.ENTER)

browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')

browser.assert_(that.number_of_elements('[id^=issue_]:not([id$=_link])', value=25))

browser.quit()
