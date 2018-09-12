import unittest
from selenium import webdriver
import webpage


class WebSiteTests(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        print('setUp')
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.get("https://www.ebay.com")

    def test01_main_page_title(self):
        print('test_main_page_is_up')
        main_page = webpage.MainPage(self.driver)
        assert main_page.is_title_matches(), "ebay main page title doesn't match"
        main_page.click_sign_in_link()

    def test02_user_singed_in(self):
        print('test_user_singed_in')
        login_page = webpage.LoginPage(self.driver)
        login_page.perform_login()
        today_page = webpage.TodayPage(self.driver)
        assert today_page.verify_user_signed_in(), "Failed to sign in"

    def test03_categories_drop_downs(self):
        print('test_categories_drop_downs')
        today_page = webpage.TodayPage(self.driver)
        assert today_page.select_from_categories_drop_downs_and_search(), "Shop by Category is not found"

    def test04_search_for_a_book(self):
        print('test_search_for_a_book')
        search_page = webpage.SearchPage(self.driver)
        assert search_page.search_for_book(), "Add book to cart not found"

    def test05_invalid_email_on_checkout(self):
        print('test_invalid_email')
        checkout = webpage.CheckOutPage(self.driver)
        assert checkout.verify_invalid_email_message(), "Invalid email message is not displayed"

    @classmethod
    def tearDownClass(inst):
        print('tearDown')
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()
