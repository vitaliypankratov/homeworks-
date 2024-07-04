from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Firefox()

    # driver.maximize.window()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)
    driver.find_element(By.TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()