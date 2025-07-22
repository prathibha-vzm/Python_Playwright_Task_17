import pytest                                      # For writing and running test cases
from playwright.sync_api import TimeoutError       # To handle Playwright timeout errors
from zenportal.pages.base_page import BasePage     # Base class with common page methods
from zenportal.pages.login_page import LoginPage   # Page class for login functionality
from zenportal.pages.dashboard_page import LogOut  # Page class for Logout functionality
import json                                        # For reading or writing JSON data

                                                              # Open the JSON file containing test data
with open("C:/Users/91956/PycharmProjects/Playwright/zenportal/utility/test_data.json") as json_file:
    data = json.load(json_file)["login_tests"]                # Load the JSON data and extract 'login_tests' section
    

                                                              # Adding marker login_test
@pytest.mark.login_test
@pytest.mark.parametrize("data_set",data)                     # Passing the test data one by one through parametrization
def test_login_functionality(page,data_set):
    # Arrange                                                 # Creating object for the classes
    base_object = BasePage(page)
    login_object = LoginPage(page)
    logout_object = LogOut(page)
    # Act                                                    # Passing data sets from test_data.json
    base_object.navigate(data_set["url"])
    login_object.enter_username(data_set["username"])
    login_object.enter_password(data_set["password"])

    login_object.check_remember_me()                        # calling the method to click on remember me checkbox
    validation=login_object.click_login()                   # Passing the result for test case from the method login to validate the login credentials
    # Assert
    if validation=="pass":                                  # To reduce the execution time while test run validated the results here
        try:                                                # if the login is passed/valid credentials this will get executed
            page.get_by_role("button", name="Close popup").click()                   # To close the pop-up appears on the page
            page.wait_for_url("https://v2.zenclass.in/dashboard", timeout=3000)      # Explicit wait to fetch the URL
            page.screenshot(
                path=r"/zenportal/reports/screenshots/assert_successful_login.png")  # Capturing the Dashboard and store in screenshot directory
            assert page.url == (data_set["expected_url"])                            # Asserting the Dashboard with URL
            logout_object.logout_functionality()                                     # Logout functionality is called to log out from dashboard page
            assert page.url=="https://v2.zenclass.in/login"                          # Validating the Logout with login page URL
        except TimeoutError:                                                         # When login failed this will execute
            print("**Failed to Login**")
    else:
        print("Unsuccessful Login")                                                   # Once the credentials are invalid it will execute this and move on to next test run







