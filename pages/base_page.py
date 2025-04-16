# Base page object with common functionality
from seletools.actions import drag_and_drop
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import BLOCKER


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, entity):
        if isinstance(entity, WebElement):
            return entity
        self.wait_for(EC.presence_of_element_located(entity))
        return self.driver.find_element(*entity)

    def get_elements_kit(self, locator):
        self.wait_for(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def get_current_url(self):
        return self.driver.current_url

    def click_element(self, entity):
        element = self.get_element(entity)
        self.wait_for(EC.element_to_be_clickable(element))
        if self.driver.name == 'firefox':
            self.click_element_firefox(element)
        else:
            element.click()

    def click_element_firefox(self, element):
        while True:
            try:
                element.click()
            except ElementClickInterceptedException as error:
                if BLOCKER not in str(error):
                    raise ElementClickInterceptedException(error)
            else:
                break

    def fill_in(self, locator, *values):
        self.get_element(locator).send_keys(values)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView()', element)
        self.wait_for(EC.visibility_of(element))

    def wait_for(self, event, timeout=10, until=''):
        getattr(WebDriverWait(self.driver, timeout), f'until{until}')(event)

    def drag_to(self, element, target):
        drag_and_drop(self.driver, element, target)  # used seletools function to avoid selenium bug with dragndrop

    def format_locator(self, locator, value):
        method, pattern = locator
        return method, pattern.format(value)
