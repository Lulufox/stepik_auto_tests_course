from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    print('num1 = ' + num1)
    print('num2 = ' + num2)
    print(num1 + num2)
    res = int(num1) + int(num2)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_visible_text(str(res))
    

    # Отправляем заполненную форму
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button")
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