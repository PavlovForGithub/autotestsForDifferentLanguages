# encoding utf8
from selenium import webdriver
import time
import unittest


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_css_selector("input.form-control.first[required]")
    name.send_keys("Name")
    secondName = browser.find_element_by_css_selector("input.form-control.second[required]")
    secondName.send_keys("Second Name")
    email = browser.find_element_by_css_selector("input.form-control.third[required]")
    email.send_keys("email@mail.com")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться,ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestClass(unittest.TestCase):
    def test_fist(self):
        link_first = "http://suninjuly.github.io/registration1.html"
        welcome_text = link_t(link_first)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_second(self):
        link_second = "http://suninjuly.github.io/registration2.html"
        welcome_text = link_t(link_second)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
