import unittest
from selenium import webdriver
from Pages.homepage import HomePage
from Pages.resultpage import ResultPage
from Tests.BaseTest import BaseTest


class MyTestCase(BaseTest):
    def test_search(self):
        home = HomePage(self.driver)
        # self.assertTrue(home.is_page_loaded())
        assert home.is_page_loaded() is True
        home.select_video_from_dropdown()
        home.set_exact_flag("false")
        home.type_search_request("milf")
        home.click_submit()
        result_page = ResultPage(self.driver)
        #self.assertTrue(result_page.display_movies("milf"))


if __name__ == '__main__':
    unittest.main()