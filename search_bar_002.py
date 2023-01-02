import inspect
import unittest
from selenium import webdriver
import pages
from selenium.webdriver.common.by import By
import general_results


class SearchBar(unittest.TestCase):

    path_to_driver = "H:\ChromeDriver\chromedriver.exe"

    @classmethod
    def setUpClass(cls) -> None:
        file_name = str(__class__.__name__) + ".json"
        general_results.prepare_test_result_json(file_name)

    def setUp(self) -> None:
        self.site_name = "https://www.python.org/"
        self.driver = webdriver.Chrome(SearchBar.path_to_driver)
        self.driver.get(self.site_name)
        self.page = pages.MainPage()
        self.page_tests = pages.PageElementsTesting(self.page, self.driver)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        del self.page_tests
        del self.page

    def test_step_1_search_bar_exist(self):
        element_id = (By.ID, "id-search-field")
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        self.page_tests = pages.PageElementsTesting(self.page, self.driver)
        actual_value = self.page_tests.if_exist(element_id, class_method_names)
        self.assertEqual(True, actual_value, (str(element_id) + "does not exist"))

    def test_step_2_forwarding_after_search(self):
        element_id = (By.ID, "id-search-field")
        search_word = "pycon"
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        self.page_tests = pages.PageElementsTesting(self.page, self.driver)
        actual_value = self.page_tests.forwarding_after_search(element_id, search_word, class_method_names)
        self.assertEqual(True, actual_value, "title is wrong")
