from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url  = "https://github.com/"
driver.get(url)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")
sleep(2)

url = "https://www.saucedemo.com/"
driver.get(url)

print(driver.title)
if "Swag" in driver.title :
    driver.save_screenshot("saucedemo.com-homepage.png")

sleep(2)
driver.back()
#driver.forward() => iler almak için 
sleep(2)

driver.close
