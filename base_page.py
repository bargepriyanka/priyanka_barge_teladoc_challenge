from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown(self, locator, role):
        # element=self.wait_for_element(locator)
        # element.click()
        # select_fr = Select(self.find_element(locator))
        # Select.select_by_index(self,1)
        '''
        select_fr = Select(self.find_element(locator))
        select_fr.select_by_index(role)
        print("Executed line no 31")
        '''
        select = Select(WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)))
        select.select_by_visible_text(role)
        print("Executed line no 50")        

    def handle_confirmation_dialog(self):
        # Handle any confirmation dialog (if present)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn-primary")]')))
        confirm_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn-primary")]')
        confirm_button.click()          
