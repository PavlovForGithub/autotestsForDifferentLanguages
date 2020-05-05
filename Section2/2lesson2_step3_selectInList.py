# encoding utf8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time



try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(int(num1)+int(num2)))

    browser.find_element_by_css_selector("button[type=submit]").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
