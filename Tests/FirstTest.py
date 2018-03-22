import unittest
from selenium import webdriver
from Pages import HomePage


class MyTestCase(unittest.TestCase):
    def test_search(self):
        home = HomePage(self.driver)
        result = home.search("automated testing infro")
        assert "automated" in result.first_link
        self.assertEqual("$0.00", "")


if __name__ == '__main__':
    unittest.main()