from selenium.webdriver.common.by import By
from base_page import BasePage

class WebTablesPage(BasePage):
    url = "http://www.way2automation.com/angularjs-protractor/webtables/"

    # Locators
    add_user_button = (By.XPATH, "//button[text()=' Add User']")
    firstname_input = (By.XPATH, "//input[@name='FirstName']")
    lastname_input = (By.XPATH, "//input[@name='LastName']")
    username_input = (By.XPATH, "//input[@name='UserName']")
    password_input = (By.XPATH, "//input[@name='Password']")
    customer_radio = (By.XPATH, "//input[@type='radio' and @value='15']")
    role_dropdown = (By.XPATH, "//select[@name='RoleId']")
    email_input = (By.XPATH, "//input[@name='Email']")
    mobile_input = (By.XPATH, "//input[@name='Mobilephone']")
    save_button = (By.XPATH, "//button[@class='btn btn-success']")
    table = (By.XPATH, "//tr[contains(@class,'smart-table-data-row')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to(self):
        self.open_url(self.url)

    def add_new_user(self, firstname, lastname, username, password, role, email, mobile):
        self.click_element(self.add_user_button)
        self.enter_text(self.firstname_input, firstname)
        self.enter_text(self.lastname_input, lastname)
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click_element(self.customer_radio)
        self.select_dropdown(self.role_dropdown, role)
        self.enter_text(self.email_input, email)
        self.enter_text(self.mobile_input, mobile)
        self.click_element(self.save_button)

    def is_user_added(self, username):
        print(f"Status for user:{username}")
        table_rows = self.driver.find_elements(*self.table)
        for row in table_rows:
            return True if username in row.text else False

    def delete_user(self, username):
        delete_button_xpath = f"//tr[contains(., '{username}')]/td[last()]/button"
        
        delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
        delete_button.click()

    def is_user_deleted(self, username):
        print(f"Status for user:{username}")
        table_rows = self.driver.find_elements(*self.table)
        for row in table_rows:
            return True if not username in row.text else False

     
