# encoding utf8
import math
import os

from selenium import webdriver
import time


try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))
    print(y)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
