# Python_Playwright_Task_17
* Playwright, AAA, POM, Pytest, DDTF, Explicit wait, Exception handling
* Testing Tool used - Playwright
* Test Structure -AAA -Arrange Act and Assert
* Frameworks
1. DDTF (Data Driven Testing Framework) to store test data in a seperate Json file for better data management.
2. Pytest as Test runner
3. POM (Page Object Model)
4. Wait - Used Explicit wait to handle elements visibility.
5. Exception handling - Handled the TimeoutError for uniterrupted test runs.
6. OOPS concept 
* Project Structure:- POM 
1. Pages - The Login page elements are located here and values are passed from test logic.
2. Test - This package contains test logics to validate elements and implemented DDTF by incorporating input data from JSON and followed with AAA test structure.
3. conftest - To create the environment to run the test. This file is located under test package
4. Utility - This package contains Json file contains test data. In test_data.json 4 set of test cases are added.
5. reports - This directory contais report.html generated after test execurtion and screenshots captured during test runs.
6. requiremenets.txt - This file contains the packages needed for this project
7. pytest.ini - Configuration file to customize Pytest options.  

