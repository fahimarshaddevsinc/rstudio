import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = None
url="https://login.rstudio.cloud/"

@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    if browser == "chrome":
        s=Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == "firefox":
        s=Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser == "edge":
        s=Service(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=s)

    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="class", autouse=True)
# def url(request):
#     return request.config.getoption("--url")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://rstudio.cloud/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "RStudio Test Results"
