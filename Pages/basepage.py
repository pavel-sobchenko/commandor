from abc import abstractmethod
from selenium import webdriver
from Pages.PageElements.search_region import SearchRegion


class BasePage(object):

    """ All page objects inherit from this """
    def __init__(self, driver):
        self._search_region = SearchRegion(driver)
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    def get_title(self):
        return self.driver.title

    def get_search_region(self):
        return self._search_region

    def is_page_loaded(self):
        return self.get_search_region().is_element_visible()

    """ Regions define functionality available throughall page objects """
    @property
    def search(self):
        pass
        #from search import SearchRegion
        #return SearchRegion(self.driver)


class InvalidPageException(Exception):
    """ Throw this exception when you don’t find the correct page """
    pass

#get_title

#wait_for_page_laoded

#ensure_page_loaded