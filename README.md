# CapstoneProject-Selenium-Python-Pytest
Capstone project using Selenium with Python and Pytest framework
**Mini Project: Web Application Testing in Visual Studio Code**

This mini project automates the testing of a web application using Selenium and Pytest in Visual Studio Code. The script verifies page titles, checkbox states, and file upload functionality.

**Prerequisites**

Ensure the following are installed:

- **Python**
- **Selenium**
- **Pytest**
- **Google Chrome Browser**
- **ChromeDriver** (placed in D:\\WebAppTesting\\drivers)

**Project Structure**

D:\\WebAppTesting\\

├── drivers\\ # Contains WebDriver executables

├── files\\ # Contains test files for upload

├── pages\\ # Page Object Model classes

│ ├── \__init_\_.py

│ ├── checkboxes_page.py

│ ├── file_upload_page.py

│ ├── homepage.py

├── tests\\ # Test cases using Pytest

│ ├── \__init_\_.py

│ ├── test_web_app.py

**Test Execution and Review**

1. Clone the repository to a local machine.
2. Open the project in Visual Studio Code.
3. Run the test suite using the Pytest command:

pytest tests/test_web_app.py --html=report.html --self-contained-html --log-level=INFO --log-file=logfile.log

1. Open report.html to showcase the test results.

**Logging and Reporting**

- Logs are stored in logfile.log.
- Open and review report.html to illustrate how test results are displayed.
- Highlight error handling and debugging mechanisms.

**Summary**

- The test cases validate page navigation, checkbox selection states, and file upload functionality.
- Assertions are used to verify expected results in each test scenario.
- The project follows a structured framework with clear separation of concerns.
- Logs and reports provide detailed insights into test execution and results.
