# ecommerce-automation-testing-framework
Python-based E-Commerce automation framework for Web, API & Database testing using Selenium, PyTest, Requests, MySQL, Jenkins, and Allure.
# E-Commerce Automation Testing Framework

A Python-based automation testing framework for testing an e-commerce application across the **web, API, and database layers**.

The project uses **Selenium, PyTest, Python, Requests, MySQL, Jenkins, and Allure** to automate different types of testing and generate test reports.

## What this project covers

* **Web Automation** – Automated browser workflows using Selenium WebDriver.
* **API Testing** – REST API testing using Python Requests and Postman.
* **Database Testing** – Validates application data using MySQL.
* **Smoke Testing** – Checks whether the main application features are working.
* **Regression Testing** – Runs existing test cases to make sure new changes do not break existing functionality.
* **Functional Testing** – Tests individual application features.
* **Test Reporting** – Generates Allure and HTML reports for analyzing test results.
* **CI/CD** – Supports automated test execution through Jenkins pipelines.

## Tech Stack

**Programming:** Python
**Web Automation:** Selenium WebDriver
**Testing Framework:** PyTest
**API Testing:** Python Requests, Postman
**Database:** MySQL
**CI/CD:** Jenkins
**Reporting:** Allure, HTML Reports
**Version Control:** Git, GitHub

## Project Structure

```text
e-commerce-automation/
│
├── tests/
│   ├── web/
│   ├── api/
│   ├── database/
│   ├── smoke/
│   ├── regression/
│   └── functional/
│
├── pages/
│   └── page_objects/
│
├── config/
│
├── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## Test Dashboard

The project includes a Streamlit-based dashboard to monitor test execution and results.

The dashboard provides sections for:

* Test Execution
* API Testing
* Database Testing
* Reports
* Defects
* Configuration

### Current Test Execution

The current dashboard shows:

| Result      | Tests |
| ----------- | ----: |
| Total Tests |   128 |
| Passed      |   112 |
| Failed      |    16 |
| Skipped     |     0 |

**Pass Rate:** 87.5%

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/e-commerce-automation.git
cd e-commerce-automation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the test suite

```bash
pytest
```

### 4. Run a specific test category

```bash
pytest -m smoke
```

```bash
pytest -m regression
```

```bash
pytest -m functional
```

### 5. Generate an HTML report

```bash
pytest --html=reports/report.html
```

## Reporting

Test execution results can be reviewed through **HTML and Allure reports**. These reports help identify passed and failed test cases and make it easier to analyze defects.

## CI/CD

Jenkins can be configured to automatically execute the PyTest test suite whenever new code is pushed to the repository.

This allows automated testing to become part of the development workflow instead of running tests manually every time.

## What I Learned

Through this project, I worked with:

* Selenium WebDriver automation
* PyTest test organization and markers
* REST API automation
* Database validation using MySQL
* Smoke, regression, and functional testing
* Test reporting
* Jenkins CI/CD concepts
* Page Object Model
* Git and GitHub

## Future Improvements

* Add more end-to-end e-commerce test scenarios
* Increase API and database test coverage
* Integrate the framework with a cloud testing platform
* Improve Jenkins pipeline automation
* Add automated email/Slack notifications for test results

## Author

**Dharti Ghodke**

B.Tech – Artificial Intelligence & Data Science

GitHub: `github.com/dhartighodke-droid`
