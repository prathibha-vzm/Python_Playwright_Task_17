from playwright.sync_api import Page    # To import the sync.api
                                        # BasePage class containing common page methods
class BasePage:                      
    def __init__(self,page: Page):      # Constructor and page instance variable is defined
        self.page=page
                                        # Method to navigate to a given URL
    def navigate(self,url):
        self.page.goto(url)

