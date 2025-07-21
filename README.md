# Python_Playwright_Task_17
* Playwright, AAA, POM, Pytest, DDF, Explicit wait, Exception handling
* Testing Tool used - Playwright
* Test Structure -AAA -Arrange Act and Assert
* Frameworks
1. DDTF to store test data in a seperate Json file for better data management.
2. Pytest as Test runner
3. POM
4. Wait - Used Explicit wait to handle elements visibility.
5. Exception handling - Handled the TimeoutError for uniterrupted test runs.
* POM :
1. Pages - The Login page elements are located here and values are passed from test logic.
2. Test - This package contains test logics to validate elements and implemented DDT by incorporating input data from JSON and followed with AAA test structure.
3. Utility - This package contains Json file contains test data.
4. reports - This directory contais report.html generated after test execurtion and screenshots captured during test runs.

