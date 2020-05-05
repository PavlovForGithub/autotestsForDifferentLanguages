# encoding utf8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import math



try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(str(y))

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
