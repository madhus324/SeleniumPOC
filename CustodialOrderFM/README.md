**Introduction**
🔹 Automating the Custodial Order (OCDCORDS) screen using the Python Selenium

**Features**
🔹 Utilizes the Selenium WebDriver for interacting with web elements
🔹 Implements a modular and page object-oriented architecture for better code organization.
🔹 Getting into the URL through a browser
🔹 Verifying Login and Navigating to the Custodial Order (OCDCORDS) screen
🔹 Verifying Offender search and Custodial Order (OCDCORDS) screen and Adding conditions'

**Package installation for Windows users**
🔹 pip install -r requirements.txt
🔹 Pytest

**Technologies used**
🔹 Python
🔹 Selenium

**Project Structure**

|-- config
|   |-- config.ini
|   |-- browser_options.json
|-- pageobject
|   |-- base_page.py
|   |-- Add_Cust_record.py
|   |-- login_page.py
|-- reports
|   |-- screenshots
|   |-- report.html
|-- tests
|   |-- conftest.py
|   |-- test_cust_screen.py
|   |-- test_login.py
|-- utils
|   |-- customlogger.py
|   |-- ReadConfigurations.py
|-- README.md


**RunBats**
🔹 To Run single test and reports
pytest -v -rA -s tests/test_cust_screen.py --html=reports/reportcustdial.html

🔹 To Run all test and reports
pytest -v -rA -s tests--html=reports/report.html
