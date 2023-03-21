from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep 


driver = webdriver.Chrome()

url = "https://github.com/"
driver.get(url)
driver.maximize_window()
searchInput = driver.find_element(By.NAME,"q")
sleep(1)
searchInput.send_keys("python")
sleep(2)
searchInput.send_keys(Keys.ENTER)
sleep(2)
# result = driver.find_elements(By.XPATH,"/html/body")
# for element in result:
#    print(element.text)

while True:
    continue    


driver.close

