from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']").click()
browser.switch_to.alert.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_given = browser.find_element(By.CSS_SELECTOR, '#input_value').text
result = calc(x_given)
browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(result)
browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(20)
browser.quit()