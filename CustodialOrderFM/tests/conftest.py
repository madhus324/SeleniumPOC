import os.path
import time
from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities import ReadConfigurations
driver = None
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService



@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser = ReadConfigurations.read_config("basic info", "browser")
    global driver
    if browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()

    else:
        print("provide a valid browser name from this list Chrome/Firefox/Edge")
    driver.maximize_window()
    web_url = ReadConfigurations.read_config("basic info", "url")
    driver.get(web_url)
    wait = WebDriverWait(driver, timeout=10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    driver.quit()
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://qa.elitev5.com/#/login"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
