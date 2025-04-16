import pytest
import requests
from selenium import webdriver

from config import API_CREATE_USER, API_DELETE_USER, BROWSERS, MAIN_PAGE
from helpers import get_user_data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.recover_page import RecoverPage


@pytest.fixture(scope='function')
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def recover_page(driver):
    return RecoverPage(driver)


@pytest.fixture(scope='function', params=BROWSERS, ids=BROWSERS)
def driver(request):
    name = request.param
    options = getattr(webdriver, f'{name}Options')()
    for argument in BROWSERS[name]:
        options.add_argument(argument)
    driver = getattr(webdriver, name)(options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()


# Test user. Deletes after use
@pytest.fixture(scope='session')
def test_user():
    user_data = get_user_data()
    token = requests.post(url=API_CREATE_USER, data=user_data).json().get('accessToken')
    del user_data['name']
    yield user_data  # email & password
    requests.delete(url=API_DELETE_USER, headers={'Authorization': token})
