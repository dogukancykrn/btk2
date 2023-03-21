from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestCasesler():

 def login (self) :
      driver = webdriver.Chrome()
      driver = webdriver.Chrome(ChromeDriverManager().install())
      driver.maximize_window()    

      url = "https://www.saucedemo.com/"
      driver.get(url)
      sleep(2)
      loginButton =driver.find_element(By.XPATH,"//*[@id='login-button']")
      loginButton.click()
      sleep(2)
      errormessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
      print("ERRORMESSAGE = Epic sadface: Username is required")
      sleep(2)

test = TestCasesler()
test.login()
        
def testcases1(self):
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()    

    url = "https://www.saucedemo.com/"
    driver.get(url)
    sleep(2)
    Username =driver.find_element(By.ID,"user-name")
    Username.send_keys("111111")
    sleep(2)
    loginButton =driver.find_element(By.XPATH,"//*[@id='login-button']")
    loginButton.click()
    sleep(2)
    errormessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
    print("ERRORMESSAGE = Epic sadface: Password is required")
    sleep(2)
test =TestCasesler()
test.testcases1()

    
def testcases2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        url = "https://www.saucedemo.com/"
        driver.get(url)
        sleep(2)
        Username = driver.find_element(By.ID,"user-name")
        Username.send_keys("locked_out_user")
        sleep(2)
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        sleep(2)
        errormessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print("ERROR MESSAGE = Sorry, this user has been locked out.")
        sleep(2)
test = TestCasesler()
test.testcases2()        
       
    
def xICON (self) :
         driver = webdriver.Chrome()
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()    

         url = "https://www.saucedemo.com/"
         driver.get(url)
         sleep(2)
         loginButton =driver.find_element(By.XPATH,"//*[@id='login-button']")
         loginButton.click()
         sleep(2)
         ICON = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
         ICON.click()
         sleep(10)         
test = TestCasesler()
test.xICON()  


def testcasesson(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        url = "https://www.saucedemo.com/"
        driver.get(url)
        sleep(2)
        Username = driver.find_element(By.ID,"user-name")
        Username.send_keys("standard_user")
        sleep(2)
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        sleep(2)
        url2 ="https://www.saucedemo.com/inventory.html"
        driver.get(url2)
        sleep(10)
test = TestCasesler()
test.testcasesson()   


while True:
    continue 