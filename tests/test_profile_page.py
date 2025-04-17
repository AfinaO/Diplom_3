import allure

from config import ORDER_HISTORY_PAGE
from pages.profile_page import ProfilePage as p_page


class TestProfilePage:

    @allure.title('Success open user profile by click on link «Личный кабинет»')
    def test_click_open_profile_page_success(self, driver, test_user):
        profile_page = p_page(driver)
        profile_page.open_profile_page(test_user)
        assert profile_page.get_message().is_displayed()

    @allure.title('Success open orders history by click on link «История заказов»')
    def test_open_orders_section_success(self, driver, test_user):
        profile_page = p_page(driver)
        profile_page.open_profile_page(test_user)
        profile_page.orders_history_link_click()
        assert profile_page.get_current_url() == ORDER_HISTORY_PAGE

    @allure.title('Success logout by click on link «Выход»')
    def test_exit_link_click_user_logout(self, driver, test_user):
        profile_page = p_page(driver)
        profile_page.open_profile_page(test_user)
        profile_page.exit_link_click()
        assert profile_page.get_entrance_title().is_displayed()
