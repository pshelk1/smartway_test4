from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self): #добавть товар в корзину
        add_link = self.browser.find_element(*ProductPageLocators.BTN_ADD)
        add_link.click()

    def show_notification_add_product(self): #проверяем исчезновение элемената нотификации
        assert not self.invisibility_of_element(*ProductPageLocators.PRODUCT_NOTIFICCATION), \
            "Элемент не исчез"


