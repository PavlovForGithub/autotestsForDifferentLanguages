import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_verify_add_to_basket_button_present(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_elements_by_css_selector("form#add_to_basket_form button[type=submit]").is_displayed(), \
        "На странице отсутствует кнопка добавления товара в корзину"
