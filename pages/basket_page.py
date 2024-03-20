import time

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_basket_empty(self): #поверяем что корзина пуста
         assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENT), \
             "В корзине нет товара"

    def check_basket(self): #поверяем что в корзине чтото есть
         assert not self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENT), \
             "В корзине есть товара"

    def delete_product_in_basket(self): #удаляем товар из корзины
        hover = self.browser.find_element(*BasketPageLocators.BASKET_LIST)
        actions = ActionChains(self.browser)
        actions.move_to_element(hover).perform()
        self.browser.find_element(*BasketPageLocators.BTN_DELETE).click()

    def show_notification_add_product(self): #проверяем исчезновение элемената нотификации
        assert not self.invisibility_of_element(*BasketPageLocators.BASKET_NOTIFICCATION), \
            "Элемент не исчез"

