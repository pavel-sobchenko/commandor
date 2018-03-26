from Pages import basepage
from Pages.basepage import InvalidPageException
from Pages import ResultPage
from Locators import search_block_locators
from Pages.PageElements.base_page_element import BasePageElement


class SearchRegion(BasePageElement):
    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_button = self.driver.find_element_by_xpath(self._search_button_locator)
        self.search_button.click()
        self.search_field = self.driver.find_element_by_id(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)


class SearchResults(basepage):
    _product_list_locator = "ul.search-results > li"
    _product_name_locator = "div.result-title a"
    _product_image_link = "div.result-url a"
    _page_title_locator = "div.page-title"
    _products_count = 0
    _products = {}
    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements_by_css_selector(self._product_list_locator)
        for product in results:
            name = product.find_element_by_css_selector(self._product_name_locator).text
            self._products[name] = product.find_element_by_css_selector(self._product_image_link)

    def _validate_page(self, driver):
        if 'Search' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ResultPage(self.driver)