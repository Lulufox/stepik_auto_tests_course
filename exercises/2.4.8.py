from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get(link)
    #text_to_be_present_in_element
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    browser.find_element(By.ID, 'book').click()

    
    selector_value = '#input_value'
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)
    
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)
    
    #browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    #browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    # Отправляем заполненную форму
    #time.sleep(1)
    button = browser.find_element(By.ID, "solve")
    #time.sleep(1)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()