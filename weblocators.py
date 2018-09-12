from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    SIGN_IN_LINK = (By.LINK_TEXT, 'Sign in')


class LoginPageLocators(object):
    USER_FIELD = (By.ID, 'userid')
    PASSWORD_FIELD = (By.ID, 'pass')
    SIGN_IN_BUTTON = (By.ID, 'sgnBt')


class TodayPageLocators(object):
    WELCOME_USER = (By.ID, 'gh-ug')
    CATEGORIES_DROP_DOWNS = (By.ID, 'gh-cat')
    SEARCH_BUTTON = (By.ID, 'gh-btn')
    SHOP_BY_CATEGORY = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Books'])[4]/following::h2[1]")


class SearchPageLocators(object):
    SEARCH_FIELD = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-btn')
    loc = "(.//*[normalize-space(text()) and normalize-space(.)='Items in search results'])[1]/following::img[1]"
    FIRST_BOOK_RESULT = (By.XPATH, loc)
    PRICE_LBL = (By.ID, 'prcIsum-lbl')


class CheckOutPageLocators(object):
    ADD_TO_CART = (By.ID, 'isCartBtn_btn')
    EMAIL_FIELD = (By.ID, 'email')
    CITY_FIELD = (By.ID, 'city')
    INVALID_EMAIL_MESSAGE = (By.ID, 'email_w')
