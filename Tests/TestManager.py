import unittest
import HtmlTestRunner
import os
#from searchproduct import SearchTest
#from homepagetest import HomePageTest

dir = os.getcwd()

#search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

#outfile = open(dir + "\SmokeTestReport.html", "w")
# runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests')
runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')

#runner.run(smoke_tests)