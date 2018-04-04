# from Pages import resultpage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basepage import BasePage, InvalidPageException
from Locators.search_block_locators import SearchBlockLocator


class HomePage(BasePage):

    def __init__(self, driver):
        self._search_block_class_locator = "Search"
        self._title_name = "Free porn"
        self._search_class_button_locator = "pt-search"
        self._search_select = "//div[@class='Search__select']"
        self._options = self._search_select + "/ul/li/a/span"
        self._exact_checkbox_locator = ".checkbox"

        super(HomePage, self).__init__(driver)
        # self._search_block_locator = SearchBlockLocator(driver)
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

    def select_video_from_dropdown(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.CLASS_NAME, self._search_class_button_locator).is_displayed())
        self.driver.find_element(By.CLASS_NAME, self._search_class_button_locator).click()
        WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element(By.XPATH, self._search_select).is_displayed())
        self.driver.find_element(By.XPATH, self._search_select).click()
        for element in self.driver.find_elements(By.XPATH, self._options):
            if element.get_attribute("innerHTML") == "Video":
                element.click()
                break

    def set_exact_flag(self, value):
        if self.driver.find_element(By.CSS_SELECTOR, self._exact_checkbox_locator).get_attribute("checked") != value:
            self.driver.find_element(By.CSS_SELECTOR, self._exact_checkbox_locator).click()

    def search(self, param):
        pass
        # self.driver.find_element_by_id("gbqfa").send_keys(param)
        # return resultpage(self.driver)
