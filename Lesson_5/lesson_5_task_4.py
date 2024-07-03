import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()

    # driver.maximize.window()
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # ждем пока модальное окно не появится и кнопка "CLOSE" не станет кликабельной
    wait = WebDriverWait(driver, 10)
    modal_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .close-button")))

    time.sleep(3)
    # нажимаем кнопку "CLOSE" в модальном окне
    close_button.click()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()