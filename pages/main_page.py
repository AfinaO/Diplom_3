import random
import allure
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element as text_in_element,
    invisibility_of_element_located as element_invisible,
)

from data import INGREDIENTS_INDEXES, ORDER_NUM_PREFIX, STUB
from locators import MainPageLocators as M
from locators import HeaderLocators as H
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Go to User Profile page')
    def go_to_user_profile(self):
        self.click_element(H.PERSONAL_ACCOUNT_LINK)

    @allure.step('Click on Main Page header link')
    def header_link_click(self, name):
        self.click_element(self.format_locator(H.HEADER_LINK, name))

    @allure.step('Click on link «Лента Заказов»')
    def orders_list_link_click(self):
        self.header_link_click('Лента Заказов')

    @allure.step('Click on ingredient')
    def ingredient_click(self, ingredient):
        self.scroll_to(ingredient)
        self.click_element(ingredient)

    @allure.step('Click to close ingredients details')
    def ingredient_details_close(self):
        self.click_element(M.INGREDIENT_X_BTN)
        self.wait_for(element_invisible(M.INGREDIENT_X_BTN))

    @allure.step('Click on button «Оформить заказ»')
    def place_order_btn_click(self):
        self.click_element(M.PLACE_ORDER_BTN)

    @allure.step('Click on order in the feed')
    def order_in_orders_list_click(self, number):
        self.click_element(
            self.get_order_from_orders_list(number)
        )

    @allure.step('Click to close window with order number')
    def order_number_X_click(self):
        self.click_element(M.ORDER_ID_X_BTN)

    @allure.step('Get ingredient')
    def get_ingredient(self, slicer=slice(None)):
        return random.choice(
            self.get_elements_kit(M.INGREDIENTS_LINKS)[slicer]
        )

    @allure.step('Get ingredient details window title')
    def get_ingredient_details_title(self):
        return self.get_element(M.INGREDIENT_DETAILS_TITLE)

    @allure.step('Get ingredient counter')
    def get_ingredient_counter(self, ingredient):
        index = self.get_elements_kit(M.INGREDIENTS_LINKS).index(ingredient)
        return self.get_elements_kit(M.INGREDIENTS_COUNTERS)[index]

    @allure.step('Get basket for order')
    def get_basket(self):
        return self.get_element(M.BASKET)

    @allure.step('Get order number')
    def get_order_number(self):
        self.wait_for(text_in_element(M.ORDER_ID, text_=STUB), until='_not')
        return self.get_element(M.ORDER_ID)

    @allure.step('Get order details text')
    def get_order_details_text(self):
        return self.get_element(M.ORDER_DETAILS_TXT)

    @allure.step('Get order from the feed')
    def get_order_from_orders_list(self, number):
        if not number.startswith(ORDER_NUM_PREFIX):
            number = ORDER_NUM_PREFIX + number
        return self.get_element(
            self.format_locator(M.ORDER_IN_LIST, number)
        )

    @allure.step('Get order number from section «В работе»')
    def get_order_number_in_progress_section(self, number):
        return self.get_element(
            self.format_locator(M.ORDER_IN_PROGRESS, number)
        )

    @allure.step('Get orders counter')
    def get_orders_counter(self, name):
        return self.get_element(self.format_locator(M.ORDERS_COUNTER, name))

    @allure.step('Get main page title')
    def get_section_title(self, name):
        return self.get_element(self.format_locator(M.SECTION_TITLE, name))

    @allure.step('Add ingredient to the basket')
    def add_ingredient_to_basket(self, ingredient, basket):
        self.drag_to(ingredient, basket)

    @allure.step('Create order and get its order number')
    def make_order(self, login_page, test_user):
        self.go_to_user_profile()
        login_page.login(**test_user)
        basket = self.get_basket()
        for slicer in INGREDIENTS_INDEXES.values():
            self.add_ingredient_to_basket(self.get_ingredient(slicer), basket)
        self.place_order_btn_click()
        order_number = self.get_order_number().text
        self.order_number_X_click()
        return order_number
