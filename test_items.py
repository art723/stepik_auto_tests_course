from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), 'WARNING: Basket button NOT found!'
