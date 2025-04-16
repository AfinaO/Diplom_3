# All locators divided by pages
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    ENTER_BTN = By.XPATH, '//button[text()="Войти"]'
    ENTRANCE_TITLE = By.XPATH, '//h2[text()="Вход"]'
    PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'
    RECOVER_PASS_LINK = By.XPATH, '//a[text()="Восстановить пароль"]'


class HeaderLocators:
    HEADER_LINK = By.XPATH, '//p[text()="{}"]/ancestor::a'
    PERSONAL_ACCOUNT_LINK = By.XPATH, '//a[@href="/account"]'


class RecoverPageLocators:
    EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    ENTER_CODE_LABEL = By.XPATH, '//label[text()="Введите код из письма"]'
    SHOW_PASS_BTN = By.XPATH, '//div[contains(@class, "input__icon")]'
    PASSWORD_FRAME = By.XPATH, '//label[text()="Пароль"]/ancestor::div[1]'
    RECOVER_BTN = By.XPATH, '//button[text()="Восстановить"]'
    RECOVER_PASS_TITLE = By.XPATH, '//h2[text()="Восстановление пароля"]'


class ProfilePageLocators:
    EXIT_LINK = By.XPATH, '//button[text()="Выход"]'
    MESSAGE = By.XPATH, '//p[text()="В этом разделе вы можете изменить свои персональные данные"]'
    ORDER_NUMBER = By.XPATH, '//li[contains(@class, "OrderHistory_listItem") and position()=1]//p[contains(@class, "digits")]'
    ORDERS_HISTORY_LINK = By.XPATH, '//a[text()="История заказов"]'


class MainPageLocators:
    BASKET = By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]'
    INGREDIENT_DETAILS_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'
    INGREDIENT_X_BTN = By.XPATH, '//h2[text()="Детали ингредиента"]/ancestor::div/button'
    INGREDIENTS_COUNTERS = By.XPATH, '//p[contains(@class, "counter")]'
    INGREDIENTS_LINKS = By.XPATH, '//a[contains(@class, "BurgerIngredient")]'
    ORDER_DETAILS_TXT = By.XPATH, '//p[text()="Cостав"]'
    ORDER_ID = By.XPATH, '//p[text()="идентификатор заказа"]/ancestor::div/h2'
    ORDER_ID_X_BTN = By.XPATH, '//p[text()="идентификатор заказа"]/../../button'
    ORDER_IN_LIST = By.XPATH, '//p[text()="{}"]'
    ORDER_IN_PROGRESS = By.XPATH, '//ul[contains(@class, "orderListReady")]//li[text()="{}"]'
    ORDERS_COUNTER = By.XPATH, '//p[text()="{}"]/../p[2]'
    PLACE_ORDER_BTN = By.XPATH, '//button[text()="Оформить заказ"]'
    SECTION_TITLE = By.XPATH, '//h1[text()="{}"]'
