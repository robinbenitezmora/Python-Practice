from selenium import webdriver
import os

def startBot():
    # Set the path to the chromedriver
    chromedriver = "C:/Users/your_user_name/Downloads/chromedriver_win32/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver

    # Open the browser
    driver = webdriver.Chrome(chromedriver)

    # Open the website
    driver.get("https://www.facebook.com")

    # Find the username field
    username = driver.find_element_by_id("email")

    # Enter your username
    username.send_keys("your_username")

    # Find the password field
    password = driver.find_element_by_id("pass")

    # Enter your password
    password.send_keys("your_password")

    # Find the login button
    login = driver.find_element_by_id("loginbutton")

    # Click the login button
    login.click()

startBot()
