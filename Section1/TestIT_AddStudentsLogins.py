# encoding utf8
from selenium import webdriver
import time

link = "https://testit.geekbrains.ru/admin/users"

try:
    browser = webdriver.Chrome()
    browser.get("https://testit.geekbrains.ru/admin/users")
    input1 = browser.find_element_by_css_selector("input[type='text']")
    input1.send_keys("admin")
    pas = browser.find_element_by_css_selector("input[type='password']")
    pas.send_keys("aquedoy5Ui8iev2Eesaa")
    login = browser.find_element_by_css_selector("button[type = 'submit']")
    login.click()
    # add users
    time.sleep(2)

    with open("studentsListForTestit.txt") as studentsList:
        for student in studentsList:
            addButton = browser.find_element_by_css_selector("button[type='submit']")
            addButton.click()
            fixStud = student.strip().replace(" ", "")
            userName = browser.find_element_by_css_selector("input#userName")
            userName.send_keys(fixStud)
            password = browser.find_element_by_css_selector("input#password")
            password.send_keys(fixStud + "1!")
            email = browser.find_element_by_css_selector("input#email")
            email.send_keys(fixStud + "@mail.ru")
            displayName = browser.find_element_by_css_selector("input#displayName")
            displayName.send_keys(student.strip())
            login = browser.find_element_by_css_selector("button[type = 'submit']")
            time.sleep(1)
            login.click()
            time.sleep(3)
finally:
    time.sleep(30)
    browser.quit()
