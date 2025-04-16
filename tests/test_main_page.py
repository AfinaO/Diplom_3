import allure
import pytest


class TestMainPage:

    @allure.title('Successful move by the links on the main page')
    @pytest.mark.parametrize('link_name, title_name',
                             [('Конструктор', 'Соберите бургер'),
                              ('Лента Заказов', 'Лента заказов')]
                             )
    def test_header_link_switch_success(self, main_page, link_name, title_name):
        main_page.go_to_user_profile()
        main_page.header_link_click(link_name)
        assert main_page.get_section_title(title_name).is_displayed()

    @allure.title('Test click on ingredient opens details window')
    def test_ingredient_open_details(self, main_page):
        main_page.ingredient_click(main_page.get_ingredient())
        assert main_page.get_ingredient_details_title().is_displayed()

    @allure.title('Test close details window')
    def test_ingredient_close_details(self, main_page):
        main_page.ingredient_click(main_page.get_ingredient())
        main_page.ingredient_details_close()
        assert not main_page.get_ingredient_details_title().is_displayed()

    @allure.title('Test success increase ingredients counter')
    def test_add_ingredient_to_order_increase_counter(self, main_page):
        ingredient = main_page.get_ingredient()
        counter_before = main_page.get_ingredient_counter(ingredient).text
        main_page.add_ingredient_to_basket(ingredient, main_page.get_basket())
        counter_after = main_page.get_ingredient_counter(ingredient).text
        assert int(counter_before) + 1 == int(counter_after)

    @allure.title('Test success make order by authorized user')
    def test_logged_user_make_order_success(self, main_page, login_page, test_user):
        assert main_page.make_order(login_page, test_user)

    @allure.title('Test success click on order opens details window')
    def test_order_click_open_details(self, login_page, main_page, test_user):
        order_number = main_page.make_order(login_page, test_user)
        main_page.orders_list_link_click()
        main_page.order_in_orders_list_click(order_number)
        assert main_page.get_order_details_text().is_displayed()

    @allure.title('Test success orders from history shows in the feed')
    def test_order_from_history_appears_in_orders_list(
            self, login_page, main_page, profile_page, test_user
    ):
        main_page.make_order(login_page, test_user)
        main_page.go_to_user_profile()
        profile_page.orders_history_link_click()
        order_number = profile_page.get_order_number().text
        main_page.orders_list_link_click()
        assert main_page.get_order_from_orders_list(order_number).is_displayed()

    @allure.title('Test success increase order counters «за всё время» и «за сегодня»')
    @pytest.mark.parametrize('name', ['Выполнено за все время:', 'Выполнено за сегодня:'])
    def test_increasing_orders_counters(self, login_page, main_page, test_user, name):
        main_page.orders_list_link_click()
        counter_before = main_page.get_orders_counter(name).text
        main_page.make_order(login_page, test_user)
        main_page.orders_list_link_click()
        counter_after = main_page.get_orders_counter(name).text
        assert int(counter_before) + 1 == int(counter_after)

    @allure.title('Test success order number appears in section «В работе»')
    def test_new_order_number_appears_in_progress_section(self, login_page, main_page, test_user):
        order_number = main_page.make_order(login_page, test_user)
        main_page.orders_list_link_click()
        assert main_page.get_order_number_in_progress_section(order_number).is_displayed()
