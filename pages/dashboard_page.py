from zenportal.pages.base_page import BasePage # Base class with common page methods

# LogOut class inheriting from BasePage
class LogOut(BasePage):
    def __init__(self, page):
        super().__init__(page)         # Initialize the BasePage with the current page instance
        # Defining the elements with its locators
        self.profile_icon=page.locator(".profile-click-icon-div")
        self.logout_text=page.get_by_text("Log out")

    def logout_functionality(self):
        self.profile_icon.click()                                                 # To click on profile icon
        self.logout_text.click()                                                  # To click on logout text
        self.page.wait_for_url("https://v2.zenclass.in/login", timeout=5000)  # To wait for the logot process
        self.page.screenshot(                                                     # To capture the logout page
            path=r"/zenportal/reports/screenshots/assert_successful_logout.png")
