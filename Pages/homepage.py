# from Pages import resultpage
from selenium.webdriver.common.by import By

from Pages.basepage import BasePage, InvalidPageException
from Locators.search_block_locators import SearchBlockLocator


class HomePage(BasePage):

    def __init__(self, driver):
        self._search_block_class_locator = "Search"
        self._title_name = "Free porn"
        super(HomePage, self).__init__(driver)
        #self._search_block_locator = SearchBlockLocator(driver)
        # self.driver = driver

    def _validate_page(self, driver):
        try:
            #driver.find_element_by_class_name(self.get_search_region().is_element_visible())
            driver.find_element(By.CLASS_NAME, self._search_block_class_locator).is_displayed()
        except:
            raise InvalidPageException("Home Page not loaded")

    def is_page_loaded(self):
        return self.driver.find_element(By.CLASS_NAME, self._search_block_class_locator).is_displayed() \
               and self._title_name in  self.get_title()
        # return self.driver.find_element_by_class_name(self._home_page_locator).is_displayed() \
        # and self._title_name in  self.get_title()

    def search(self, param):
        pass
        # self.driver.find_element_by_id("gbqfa").send_keys(param)
        # return resultpage(self.driver)
