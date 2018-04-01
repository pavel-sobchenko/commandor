from Pages import basepage
#from Pages.basepage import InvalidPageException
#from Pages import resultpage
from Locators.search_block_locators import SearchBlockLocator
from Pages.PageElements.base_page_element import BasePageElement


class SearchRegion(BasePageElement):
    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchForVideo(self, term, exact):
        pass
        #self.search_button = self.driver.find_element_by_xpath(self._search_button_locator)
        #self.search_button.click()
        #self.search_field = self.driver.find_element_by_id(self._search_box_locator)
        #self.search_field.clear()
        #self.search_field.send_keys(term)
        #self.search_field.submit()
        #return SearchResults(self.driver)

    def is_element_visible(self, driver):
        pass
