#Добавить 3 товара в корзину и проверить их количество

from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("http://www.rushplace.com/")
#action = ActionChains(driver)
time.sleep(1)
add1 = driver.find_element_by_xpath('//*[@id="primary"]/ul/li[1]/a[2]').click()
time.sleep(1)
add2 = driver.find_element_by_xpath('//*[@id="primary"]/ul/li[2]/a[2]').click()
time.sleep(1)
add3 = driver.find_element_by_xpath('//*[@id="primary"]/ul/li[3]/a[2]').click()
time.sleep(5)
basket = driver.find_element_by_xpath('//*[@id="menu-item-31"]/a').click()
count = len(driver.find_elements_by_class_name('cart_item'))
time.sleep(5)
driver.quit()

assert count == '3'