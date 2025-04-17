import allure

from data import ACTIVE, EMAIL
from pages.recover_page import RecoverPage as r_page


class TestRestorePage:

    @allure.title('Check open recovery page from main')
    def test_open_recover_page_success(self, driver):
        recover_page = r_page(driver)
        recover_page.open_recover_page()
        assert recover_page.get_recover_pass_title().is_displayed()

    @allure.title('Check for successful email enter and click on recovery button')
    def test_input_email_and_recover_btn_click_success(self, driver):
        recover_page = r_page(driver)
        recover_page.confirm_password_change(EMAIL)
        assert recover_page.get_enter_email_code_label().is_displayed()

    @allure.title('Check for successful click on show password button')
    def test_show_pass_btn_click_field_is_active(self, driver):
        recover_page = r_page(driver)
        recover_page.confirm_password_change(EMAIL)
        frame = recover_page.get_password_frame()
        class_before = frame.get_attribute(name='class')
        recover_page.show_pass_btn_click()
        class_after = frame.get_attribute(name='class')
        assert ACTIVE not in class_before and ACTIVE in class_after
