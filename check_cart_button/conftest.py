import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")

@pytest.fixture(scope="function")
def browser(pytestconfig):
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference('intl.accept_languages', '{}'.format(pytestconfig.getoption("language")))
    ff_profile.update_preferences()
    browser = webdriver.Firefox(ff_profile)
    yield browser
    # some time to overview result
    time.sleep(5)
    # kill instance
    browser.quit()