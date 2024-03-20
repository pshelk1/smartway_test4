from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, 'a[href="/lk/basket"]')

class ProductPageLocators():
    BTN_ADD = (By.CSS_SELECTOR, 'button.btn-main')
    PRODUCT_NOTIFICCATION = (By.CSS_SELECTOR, "div[class='action-notification show']")

class BasketPageLocators():
    BASKET_ELEMENT = (By.CSS_SELECTOR, "a[class='basket-empty__btn btn-main']")
    BASKET_LIST = (By.CLASS_NAME, "accordion__list")
    BTN_DELETE = (By.CLASS_NAME, "btn__del")
    BASKET_NOTIFICCATION = (By.CSS_SELECTOR, "div[class='action-notification show']")



