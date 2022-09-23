from tests import web
from tests.web import browser

browser.open('/')

web.ecosia.query.assert_value('').type('selene').press_enter()

browser.back()

web.ecosia.query.type(' github issues').press_enter()

web.ecosia.first_result_link.assert_text(
    'https://github.com › yashaka › selene › issues'
).click()
web.github_issues.links.assert_amount(25)

browser.quit()
