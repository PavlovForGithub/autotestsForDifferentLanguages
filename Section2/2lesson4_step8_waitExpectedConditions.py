# encoding utf8
import math
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    buttonBook = browser.find_element_by_id("book")
    buttonBook.click()

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))
    print(y)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
