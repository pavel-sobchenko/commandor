import unittest
from selenium import webdriver
from Pages.homepage import HomePage
from Tests.BaseTest import BaseTest


class MyTestCase(BaseTest):
    def test_search(self):
        home = HomePage(self.driver)
        self.assertTrue(home.page_is_loaded())
        home.select_video_from_dropdown()
        home.set_exact_flag(false)
        home.type_search_request("milf")
        result_page = home.click_submit()
        self.assertTrue(result_page.display_movies("milf"))


if __name__ == '__main__':
    unittest.main()