import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time

def test_product(browser):
    link = "https://www.wildberries.ru/catalog/168095588/detail.aspx"
    page = ProductPage(browser, link)           # инициализируем, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                 # открываем страницу
    page.add_product_to_basket()                # добавляем
    page.show_notification_add_product()        # ждем исчезновения нотификации
    page.go_to_cart()                           # переходим к корзине
    pagebasket = BasketPage(browser, link)      # инициализируем
    pagebasket.check_basket_empty()             # проверяем корзину
    pagebasket.delete_product_in_basket()       # удаляем
    pagebasket.show_notification_add_product()  # ждем исчезновения нотификации
    pagebasket.check_basket()                   # проверяем что корзина пуста
