from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    selector_value = '#input_value'
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)
    
    
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)
    #time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    #time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    #time.sleep(1)

    # Отправляем заполненную форму
    #time.sleep(1)
    
    time.sleep(1)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()