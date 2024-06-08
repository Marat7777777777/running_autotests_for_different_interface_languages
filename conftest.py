from urllib import request
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, es, en etc. ")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_language': language})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    else:
        raise pytest.UsageError("--language should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

