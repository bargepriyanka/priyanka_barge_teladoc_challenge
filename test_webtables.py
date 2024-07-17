import unittest
from selenium import webdriver
from webtables_page import WebTablesPage

class TestWebTables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.page = WebTablesPage(cls.driver)
        cls.page.navigate_to()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_scenario_1_add_user(self):
        try:
            self.page.add_new_user("John", "Doe", "johndoe", "Password123", "Sales Team", "john.doe@example.com", "1234567890")
                        
            testValue = self.page.is_user_added("John")
            print(f"Printing value from test_scenario_1_user_added : {testValue}")
            self.assertTrue(testValue, msg = "User added successfully.")
        except Exception as e:
            print(f"Printing exception in test_scenario_1_add_user : {e}")        

    def test_scenario_2_delete_user(self):
        try:
            self.page.delete_user("novak")
            self.page.handle_confirmation_dialog()
            testValue = self.page.is_user_deleted("novak")
            print(f"Printing value from test_scenario_2_user_deleted : {testValue}")
            self.assertTrue(testValue, msg = "User deleted successfully !!!")
        except Exception as e:
            print(f"Printing exception in test_scenario_2_delete_user : {e}")


if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        print(f"Printing exception : {e}")
