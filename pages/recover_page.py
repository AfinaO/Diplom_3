import allure
from locators import LoginPageLocators as L
from locators import HeaderLocators as H
from locators import RecoverPageLocators as R
from pages.base_page import BasePage


class RecoverPage(BasePage):

    @allure.step('Click on Restore button')
    def recover_btn_click(self):
        self.click_element(R.RECOVER_BTN)

    @allure.step('Click on Show Password button')
    def show_pass_btn_click(self):
        self.click_element(R.SHOW_PASS_BTN)

    @allure.step('Obtain Password Recovery Form title')
    def get_recover_pass_title(self):
        return self.get_element(R.RECOVER_PASS_TITLE)

    @allure.step('Obtain Enter Code field label')
    def get_enter_email_code_label(self):
        return self.get_element(R.ENTER_CODE_LABEL)

    @allure.step('Obtain Enter Password frame')
    def get_password_frame(self):
        return self.get_element(R.PASSWORD_FRAME)

    @allure.step('Fill Email field')
    def enter_email(self, email):
        self.fill_in(L.EMAIL_INPUT, email)

    @allure.step('Open Recovery Password page')
    def open_recover_page(self):
        self.click_element(H.PERSONAL_ACCOUNT_LINK)
        self.click_element(L.RECOVER_PASS_LINK)

    @allure.step('Go to Confirm password change page')
    def confirm_password_change(self, email):
        self.open_recover_page()
        self.enter_email(email)
        self.recover_btn_click()
