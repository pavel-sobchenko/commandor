from Pages import ResultPage
from Pages.basepage import BasePage
from Pages.basepage import InvalidPageException


class HomePage(BasePage):
    _home_page_locator = ""
    def __init__(self, driver):
        #self.driver = driver
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(self._home_page_locator)
        except:
            raise InvalidPageException("Home Page not loaded")

    def search(self, param):
        self.driver.find_element_by_id("gbqfa").send_keys(param)
        return ResultPage(self.driver)

