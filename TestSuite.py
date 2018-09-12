import unittest
from mytests import WebSiteTests

# get all tests from WebSiteTests class
my_tests = unittest.TestLoader().loadTestsFromTestCase(WebSiteTests)

# create a test suite for my_tests
test_suite = unittest.TestSuite([my_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
