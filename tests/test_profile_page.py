import allure

from config import ORDER_HISTORY_PAGE


class TestProfilePage:

    @allure.title('Success open user profile by click on link «Личный кабинет»')
    def test_click_open_profile_page_success(
        self, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(login_page, test_user)
        assert profile_page.get_message().is_displayed()

    @allure.title('Success open orders history by click on link «История заказов»')
    def test_open_orders_section_success(
        self, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(login_page, test_user)
        profile_page.orders_history_link_click()
        assert profile_page.get_current_url() == ORDER_HISTORY_PAGE

    @allure.title('Success logout by click on link «Выход»')
    def test_exit_link_click_user_logout(
        self, login_page, profile_page, test_user
    ):
        profile_page.open_profile_page(login_page, test_user)
        profile_page.exit_link_click()
        assert login_page.get_entrance_title().is_displayed()
