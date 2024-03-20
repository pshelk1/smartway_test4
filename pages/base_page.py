from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_cart(self): #переход в корзину
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def is_element_present(self, how, what):
        try:
          self.browser.find_element(how, what)
        except (NoSuchElementException):
          return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def invisibility_of_element(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element((how, what)))
        except TimeoutException:
            return True
        return False

