from seleyasha.browser import Browser


class GithubIssues:
    def __init__(self, browser: Browser):
        self.links = browser.all('[id^=issue_]:not([id$=_link])')
