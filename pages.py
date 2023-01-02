import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from element import BasePageElement
from general_results import results


class MainPage:
    def __init__(self, submit_button=(By.ID, "submit"), search_field=(By.ID, "id-search-field"), title="Welcome to Python.org"):
        self.submit_button = submit_button
        self.search_field_id = search_field
        self.title = title


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class PageElementsTesting(BasePage):

    search_text_element = BasePageElement((By.ID, "id-search-field"))

    def __init__(self, page, driver):
        super().__init__(driver)
        self.title = page.title
        self.search_field_id = page.search_field_id
        self.submit_button = page.submit_button

    def __put_word_in_search_field__(self, word):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_field_id))
        element.clear()
        element.send_keys(word)

    @results
    def check_word_in_search_field(self, word):
        expected_value = word
        self.__put_word_in_search_field__(word)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_field_id))
        actual_value = element.get_attribute("value")
        return expected_value, actual_value

    def search_word(self, word):
        self.__put_word_in_search_field__(word)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.submit_button))
        element.click()

    @results
    def title_test(self):
        expected_value = self.title
        actual_value = self.driver.title
        return expected_value, actual_value

    @results
    def search_results_test(self, xpath):
        expected_value = True
        element_exist = False
        try:
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, xpath)))
            result.click()
            element_exist = True
        except Exception as e:
            print(e)
            element_exist = False
        finally:
            actual_value = element_exist

        return expected_value, actual_value

    @results
    def verify_element_existence(self, element_to_find, class_method_name):
        """verify_element_existence
        :param element_to_find: html localization of the element (selenium.webdriver.common.by By object)
        :param class_method_name: list of class and method name which called this function

        :return expected_value: any type
        :return actual_value: the same type as expected value
        :return class_method_name: list of class and method name which called this function """

        expected_value = -1
        navigation_menu_elements = self.driver.find_elements(*element_to_find)
        actual_value = len(navigation_menu_elements)
        if len(navigation_menu_elements) > 0:
            expected_value = len(navigation_menu_elements)
        return expected_value, actual_value, class_method_name

    @results
    def check_button(self, element_to_find, url, class_method_name):
        """verify functionality of a button
        :param element_to_find: html localization of the element (selenium.webdriver.common.by By object)
        :param url: url of the site after clicking button
        :param class_method_name: list of class and method name which called this function

        :return expected_value: any type
        :return actual_value: the same type as expected value
        :return class_method_name: list of class and method name which called this function """

        expected_value = url
        button = self.driver.find_element(*element_to_find)
        button.click()
        actual_value = self.driver.current_url
        return expected_value, actual_value, class_method_name

    @results
    def if_exist(self, element_id, class_method_name):
        """verify element_existence
        :param element_id: localization of the element
        :param class_method_name: list of class and method name which called this function

        :return expected_value: any type
        :return actual_value: the same type as expected value
        :return class_method_name: list of class and method name which called this function """
        expected_value = True
        actual_value = False
        try:
            element = self.driver.find_element(*element_id)
            actual_value = True
        except Exception as e:
            print(e)
            actual_value = False
        finally:
            return expected_value, actual_value, class_method_name

    @results
    def forwarding_after_search(self, element_id, search_word, class_method_name):
        """verify if searching a phrase provide forwarding to another site
        :param element_id: localization of the element
        :param search_word: phrase to search
        :param class_method_name: list of class and method name which called this function

        :return expected_value: any type
        :return actual_value: the same type as expected value
        :return class_method_name: list of class and method name which called this function """
        expected_value = "Search PyPI"
        actual_value = "False"
        try:
            search_bar = self.driver.find_element(*element_id)
            search_bar.send_keys(search_word)
            search_bar.submit()
            self.driver.implicitly_wait(5)
            actual_value = self.driver.title
        except Exception as e:
            print(e)
            actual_value = "False"
        finally:
            return expected_value, actual_value, class_method_name
