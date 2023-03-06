import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    #text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #link_with_text = browser.find_element(By.LINK_TEXT, text)
    #link_with_text.click()
	
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    
    selector_value = '#input_value'
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)
    
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    time.sleep(1)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла