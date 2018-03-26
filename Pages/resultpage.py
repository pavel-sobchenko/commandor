from Pages import basepage
from Pages.basepage import InvalidPageException


class ResultPage(basepage):
    _product_list_locator = "ul.search-results > li"
    _product_name_locator = "div.result-title a"
    _product_image_link = "div.result-url a"
    _page_title_locator = "div.page-title"
    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super(ResultPage, self).__init__(driver)
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