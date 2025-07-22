from zenportal.pages.base_page import BasePage                  # Base class with common page methods
from playwright.sync_api import TimeoutError                    # To handle Playwright timeout errors
                                                                # LoginPage class inheriting from BasePage
class LoginPage(BasePage):
    def __init__(self,page):                                    # Defining the elements with its locators
        super().__init__(page)                                  # Initialize the BasePage with the current page instance                                                        
        self.username_txt_box=page.get_by_role("textbox", name="Email")  
        self.password_txt_box=page.get_by_role("textbox", name="Password")
        self.remember_me_check_box=page.get_by_role("checkbox", name="Checkbox demo")
        self.error_msg_1=page.get_by_text("Invalid email!")
        self.error_msg_2=page.get_by_text("Password required!")
        self.error_msg_3=page.get_by_text("Email required!")
        self.login_btn=page.get_by_role("button", name="Sign in")

   #  Method to enter username after ensuring the textbox is visible
    def enter_username(self,username):
        try:
         if username:
             if self.username_txt_box.is_enabled():            # Check if username textbox is enabled
               self.username_txt_box.wait_for(state="visible") # Wait until username textbox is visible
               self.username_txt_box.fill(username)            # Fill the textbox with the provided username
        except TimeoutError:                                   # Handle in case textbox is not found in time
            print("Username Textbox not found")

    #  Method to enter username after ensuring the textbox is visible
    def enter_password(self,password):
        try:
         if password:
             if self.password_txt_box.is_enabled():            # Check if password textbox is enabled
               self.password_txt_box.wait_for(state="visible") # Wait until username textbox is visible
               self.password_txt_box.fill(password)            # Fill the textbox with the provided username
        except TimeoutError:                                   # Handle in case textbox is not found in time
            print("Password Textbox not found")

    # method to check the remember me box
    def check_remember_me(self):
        try:
            if self.remember_me_check_box.is_checked():        # If checkbox is already checked, do nothing
                pass
            else:
                self.remember_me_check_box.click()             # If checkbox is not checked, then click
        except TimeoutError:                                   # Handle in case checkbox is not found in time
            print("Checkbox not found")
          
    # Method to click on login and locate the error message and acting according to it
    def click_login(self):
        try:
            self.login_btn.wait_for(state="visible", timeout=10000)     # Waiting for the login button to visible
            self.login_btn.click()                                      # Click on login
            self.page.wait_for_timeout(5000)                            # Waiting for the error message to be appeared
            if self.error_msg_1.is_visible():                           # Error message appears when password is incorrect and printing the text
                print(self.error_msg_1.text_content())
                self.page.screenshot(                                   # To capture the screenshot when the error occurs
                    path=r"/zenportal/reports/screenshots/login_page2.png")
                return "fail"                                           # passing fail to validate
            elif self.error_msg_2.is_visible():                         # Error message appears when password is incorrect and printing the text
                print(self.error_msg_2.text_content())
                self.page.screenshot(                                   # To capture the screenshot when the error occurs
                    path=r"/zenportal/reports/screenshots/login_page3.png")
                return "fail"                                           # passing fail to validate
            elif self.error_msg_3.is_visible():                         # Error message appears when password is incorrect and printing the text
                print(self.error_msg_3.text_content())
                self.page.screenshot(                                   # To capture the screenshot when the error occurs
                    path=r"/zenportal/reports/screenshots/login_page4.png")
                return "fail"                                           # passing fail to validate
            else:
                print(f"---{self.page.title()}---")                     # To fetch the title when login is successful
                return "pass"                                           # passing pass to validate
        except TimeoutError:                                            # Handle in case no error found
            print("Login Button not found")
