from githubUserInfo import username,password
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
url = "https://github.com/"
driver.get(url)
driver.maximize_window()
sleep(2) 

searchInput = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
searchInput.click()
sleep(2)

usernameInput = driver.find_element(By.ID,"login_field")
passwordInput = driver.find_element(By.ID,"password")
sleep(2)
usernameInput.send_keys(username)
passwordInput.send_keys(password)
sleep(2)

signinButton = driver.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]")
signinButton.click()
sleep(2)



while True:
    continue


