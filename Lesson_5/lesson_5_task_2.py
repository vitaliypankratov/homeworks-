from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver = webdriver.Firefox()

try:
    count = 0
    driver.get ("http://uitestingplayground.com/dynamicid")

# клик по синей кнопке

    blue_button = driver.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()

# клик 3 раза

    for _ in range(3):
        blue_button = driver.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1
    sleep(2)
    print(count)
except Exception as ex:
    print(ex)
finally:
    driver.quit()