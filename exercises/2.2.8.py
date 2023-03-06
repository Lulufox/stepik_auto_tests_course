import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    #text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #link_with_text = browser.find_element(By.LINK_TEXT, text)
    #link_with_text.click()
	
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, '2.2.7.txt')  
    print(file_path)
    input4 = browser.find_element(By.NAME, "file")
    input4.send_keys(file_path)
    
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла