from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCases():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        
    def test_case_1(self):
        self.login("", "")
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert error_message.text == "Epic sadface: Username is required"
        
    def test_case_2(self):
        self.login("standard_user", "")
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert error_message.text == "Epic sadface: Password is required"
        
    def test_case_3(self):
        self.login("locked_out_user", "secret_sauce")
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
        
    def test_case_4(self):
        self.login("", "")
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        assert username_input.get_attribute("class") == "error"
        assert password_input.get_attribute("class") == "error"
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        close_button = self.driver.find_element(By.XPATH, "//button[@class='error-button']")
        close_button.click()
        assert "error" not in username_input.get_attribute("class")
        assert "error" not in password_input.get_attribute("class")
        assert not error_message.is_displayed()
        
    def test_case_5(self):
        self.login("standard_user", "secret_sauce")
        inventory_page_title = WebDriverWait(self.driver, 5).until(EC.title_contains("Swag Labs"))
        assert inventory_page_title == "Swag Labs"
        product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='inventory_item']"))
        assert product_count == 6
        
    def __del__(self):
        self.driver.quit()
