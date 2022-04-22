from selenium import webdriver
import pytest

from TestFramework.TestData import LogInData

chrome_path = PATHTOCHROME
firefox_path = PATHTOGECKO'
URL = 'http://automationpractice.com'
driver = None

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')

@pytest.fixture(scope='function')
def setup(request):
    global driver
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(executable_path=firefox_path, options=options)
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.quit()



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.fixture(params=LogInData.UserLogin.user)
def getData(request):
    return request.param

