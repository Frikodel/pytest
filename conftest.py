import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru")

@pytest.fixture(scope="function")
def browser(pytestconfig):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', pytestconfig.getoption("language"))
    browser = webdriver.Firefox(firefox_profile=profile)
    yield browser
    browser.quit()