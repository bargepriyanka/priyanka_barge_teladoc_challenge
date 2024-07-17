from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    # Navigate to the webpage
    driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")


    driver.set_window_size(1024, 600)
    driver.maximize_window()

    # Wait for the page to load and elements to become clickable
    WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Add User"]')))
    print("Executed line no 19")

    # Click on Add User button
    add_user_button = driver.find_element(By.XPATH, '//button[text()=" Add User"]')
    add_user_button.click()
    print("Executed line no 24")

    # Fill out the form
    firstname_field = driver.find_element(By.XPATH, '//input[@name="FirstName"]')
    firstname_field.send_keys("John")
    print("Executed line no 29")

    lastname_field = driver.find_element(By.XPATH, '//input[@name="LastName"]')
    lastname_field.send_keys("Doe")
    print("Executed line no 33")

    username_field = driver.find_element(By.XPATH, '//input[@name="UserName"]')
    username_field.send_keys("johndoe")
    print("Executed line no 37")

    password_field = driver.find_element(By.XPATH, '//input[@name="Password"]')
    password_field.send_keys("password")
    print("Executed line no 41")

    company_dropdown = driver.find_element(By.XPATH, '//input[@type="radio" and @value="15"]')
    company_dropdown.click()  # Assuming 'Company AAA' has a value of 15 for this example
    print("Executed line no 45")

    select = Select(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//tr[@class="smart-table-edit-data-cell ng-scope"]//select[@name="RoleId"]'))))
    select.select_by_visible_text("Sales Team")
    print("Executed line no 50")

      
    select_fr = Select(driver.find_element(By.XPATH, '//tr[@class="smart-table-edit-data-cell ng-scope"]//select[@name="RoleId"]'))
    select_fr.select_by_index(1)
    print("Executed line no 50")
    
    
    email_field = driver.find_element(By.XPATH, '//input[@name="Email"]')
    email_field.send_keys("abc@gmail.com")
    print("Executed line no 54")

    password_field = driver.find_element(By.XPATH, '//input[@name="Mobilephone"]')
    password_field.send_keys("9999999999")
    print("Executed line no 58")


    # Save the user
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-success"]')))

    save_button = driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
    save_button.click()
    print("Executed line no 72")
    WebDriverWait(driver, 30)

    # Wait for the new user to appear in the table
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//tr[td[text()="John"]]')))
    print("Executed line no 77")

    # Validate user addition
    new_user_row = driver.find_element(By.XPATH, '//tr[td[text()="John"]]')
    assert new_user_row.is_displayed(), "Failed to add user"

    print("Scenario 1 (Add User) executed successfully!")



    # Wait for the page to load and elements to become clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//tr[td[text()="Mark"]])/td/button/i[@class="icon icon-remove"]')))

    # Locate the user row and delete button
    user_row = driver.find_element(By.XPATH, '(//tr[td[text()="Mark"]])')
    delete_button = user_row.find_element(By.XPATH, './td/button/i[@class="icon icon-remove"]')
    delete_button.click()
    WebDriverWait(driver, 30)

    # Handle any confirmation dialog (if present)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn-primary")]')))
    confirm_button = driver.find_element(By.XPATH, '//button[contains(@class,"btn-primary")]')
    confirm_button.click()
    WebDriverWait(driver, 30)
    print("Executed line no 99")


    # Wait for user row to disappear from the table
    WebDriverWait(driver, 10).until(EC.staleness_of(user_row))

    # Validate user deletion
    try:
        driver.find_element(By.XPATH, '//tr[td[text()="Mark"]]')
        assert False, "User 'novak' still present in the table after deletion"
    except NoSuchElementException:
        pass  # User 'novak' not found, which is expected

    print("Scenario 2 (Delete User 'novak') executed successfully!")

finally:
    # Close the browser session
    driver.quit()