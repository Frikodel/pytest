from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestClass:

    def test_add_to_cart_button(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        assert EC.visibility_of_element_located((By.CLASS_NAME,'btn btn-lg btn-primary btn-add-to-basket'))
