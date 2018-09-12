from weblocators import MainPageLocators
from weblocators import LoginPageLocators
from weblocators import TodayPageLocators
from weblocators import SearchPageLocators
from weblocators import CheckOutPageLocators
from selenium.webdriver.support.ui import Select
from constants import Constants
import time


class BasePage(object):
    """This is the base class in order to initialize the base page
     Each page may call to base class"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """The Home page and its methods"""

    def is_title_matches(self):
        """Verifies that specific title appears in page title"""
        return Constants.TITLE in self.driver.title

    def click_sign_in_link(self):
        element = self.driver.find_element(*MainPageLocators.SIGN_IN_LINK)
        element.click()


class LoginPage(BasePage):

    def perform_login(self):
        element = self.driver.find_element(*LoginPageLocators.USER_FIELD)
        element.clear()
        element.send_keys(Constants.USER)
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.click()
        element.clear()
        element.send_keys(Constants.PASSWORD)
        element = self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        element.click()


class TodayPage(BasePage):
    def verify_user_signed_in(self):
        message = self.driver.find_element(*TodayPageLocators.WELCOME_USER).text
        return Constants.SINGED_IN_MESSAGE in message

    def select_from_categories_drop_downs_and_search(self):
        element = self.driver.find_element(*TodayPageLocators.CATEGORIES_DROP_DOWNS)
        element.click()
        Select(element).select_by_visible_text("Books")
        element.click()
        element = self.driver.find_element(*TodayPageLocators.SEARCH_BUTTON)
        element.click()
        category = self.driver.find_element(*TodayPageLocators.SHOP_BY_CATEGORY).text
        return Constants.SHOP_CATEGORY in category


class SearchPage(BasePage):
    def search_for_book(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)
        element.click()
        element.clear()
        element.send_keys(Constants.SEARCH_BOOK)
        element = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        element.click()
        element = self.driver.find_element(*SearchPageLocators.FIRST_BOOK_RESULT)
        element.click()
        price_text = self.driver.find_element(*SearchPageLocators.PRICE_LBL).text
        return Constants.PRICE_LBL in price_text


class CheckOutPage(BasePage):
    def verify_invalid_email_message(self):
        element = self.driver.find_element(*CheckOutPageLocators.ADD_TO_CART)
        element.click()
        element = self.driver.find_element(*CheckOutPageLocators.EMAIL_FIELD)
        element.click()
        element.clear()
        element.send_keys('aaa')
        element = self.driver.find_element(*CheckOutPageLocators.CITY_FIELD)
        element.click()
        time.sleep(4)
        invalid_email_message = self.driver.find_element(*CheckOutPageLocators.INVALID_EMAIL_MESSAGE).text
        return Constants.INVALID_EMAIL_MESSAGE in invalid_email_message






