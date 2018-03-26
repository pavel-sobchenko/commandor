from Pages import resultpage
from Pages.basepage import BasePage
from Pages.basepage import InvalidPageException


class HomePage(BasePage):
    _home_page_locator = "Search"
    _title_name = "Free porn"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(self._home_page_locator)
        except:
            raise InvalidPageException("Home Page not loaded")

    def is_page_loaded(self):
        return self.driver.find_element_by_class_name(self._home_page_locator).is_displayed() \
               and self._title_name in  self.get_title()

    def search(self, param):
        self.driver.find_element_by_id("gbqfa").send_keys(param)
        return resultpage(self.driver)

