# encoding utf8
import os

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import math

try:
    print(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("firstname")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("lastname")
    email = browser.find_element_by_name("email")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    inputFile = browser.find_element_by_id("file")
    inputFile.send_keys(file_path)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
