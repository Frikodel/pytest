from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class TestClass:

    def test_check(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        browser.get(link)
        assert EC.visibility_of_element_located((By.CLASS_NAME,'btn btn-lg btn-primary btn-add-to-basket'))
