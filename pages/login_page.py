import allure
from locators import LoginPageLocators as L
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Click on link «Восстановить пароль»')
    def restore_pass_link_click(self):
        self.click_element(L.RECOVER_PASS_LINK)

    @allure.step('Click on button «Войти»')
    def enter_button_click(self):
        self.click_element(L.ENTER_BTN)

    @allure.step('Get title of the form «Вход»')
    def get_entrance_title(self):
        return self.get_element(L.ENTRANCE_TITLE)

    @allure.step('Fill field «email»')
    def input_email(self, email):
        self.fill_in(L.EMAIL_INPUT, email)

    @allure.step('Fill field «пароль»')
    def input_password(self, password):
        self.fill_in(L.PASSWORD_INPUT, password)

    @allure.step('User login')
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.enter_button_click()
