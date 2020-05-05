# encoding utf8
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    browser.find_element_by_css_selector("input#robotCheckbox").click()
    browser.find_element_by_css_selector("input#robotsRule").click()
    browser.find_element_by_css_selector("button.btn.btn-default").click()

    print(calc(x))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
