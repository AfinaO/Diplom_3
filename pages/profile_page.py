import allure
from locators import HeaderLocators as H
from locators import ProfilePageLocators as P
from pages.base_page import BasePage
from pages.login_page import LoginPage as l_page


class ProfilePage(BasePage):

    @allure.step('Click on link «История заказов»')
    def orders_history_link_click(self):
        self.click_element(P.ORDERS_HISTORY_LINK)

    @allure.step('Click on link ссылке «Выход»')
    def exit_link_click(self):
        self.click_element(P.EXIT_LINK)

    @allure.step('Get message')
    def get_message(self):
        return self.get_element(P.MESSAGE)

    @allure.step('Get order number')
    def get_order_number(self):
        return self.get_element(P.ORDER_NUMBER)

    @allure.step('Open user profile')
    def open_profile_page(self, test_user):
        self.click_element(H.PERSONAL_ACCOUNT_LINK)
        l_page(self.driver).login(**test_user)
        self.click_element(H.PERSONAL_ACCOUNT_LINK)

    @allure.step('Get title of the form «Вход»')
    def get_entrance_title(self):
        return self.get_element(P.ENTRANCE_TITLE)
