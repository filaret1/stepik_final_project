import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',)
    parser.addoption('--language', action="store", default='en', help="Choose from langs: (en/ru/es/...)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    else:
        print("Browser<browser_name> still is not implemented")
    yield browser
    print("\nQuit browser...")
    browser.quit()