import inspect
import unittest
from selenium import webdriver
import pages
from selenium.webdriver.common.by import By
import general_results


class PythonOrgNavigationMenu(unittest.TestCase):

    path_to_driver = "H:\ChromeDriver\chromedriver.exe"

    @classmethod
    def setUpClass(cls) -> None:
        file_name = str(__class__.__name__) + ".json"
        general_results.prepare_test_result_json(file_name)

    def setUp(self) -> None:
        self.site_name = "https://www.python.org/"
        self.driver = webdriver.Chrome(PythonOrgNavigationMenu.path_to_driver)
        self.driver.get(self.site_name)
        self.page = pages.MainPage()
        self.page_tests = pages.PageElementsTesting(self.page, self.driver)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        del self.page_tests
        del self.page

    def test_step_1_NavigationMenu(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        navigation_menu_elements = (By.CSS_SELECTOR, ".navigation.menu")
        actual_value = self.page_tests.verify_element_existence(navigation_menu_elements, class_method_names)
        self.assertEqual(True, actual_value, "Navigation Menu does not exist")

    def test_step_2_AboutButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "about"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_3_DownloadsButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "downloads"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_4_DocumentationButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "documentation"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_5_CommunityButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "community"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_6_SuccessStoriesButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "success-stories"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_7_NewsButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "news"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

    def test_step_8_EventsButton(self):
        class_method_names = [self.__class__.__name__, inspect.stack()[0][3]]
        button_id = "events"
        url = self.site_name + button_id + "/"
        about_button_finder = (By.ID, button_id)
        actual_value = self.page_tests.check_button(about_button_finder, url, class_method_names)
        self.assertEqual(True, actual_value, (button_id + "button does not work"))

