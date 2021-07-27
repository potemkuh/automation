#Проверка автаризации, добавление сотрудника и удаление сотрудника

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/l")
action = ActionChains(driver)

#Автаризация
login = driver.find_element_by_id("txtUsername")
login.send_keys('Admin')
password = driver.find_element_by_id("txtPassword")
password.send_keys('admin123')
btn_login = driver.find_element_by_id("btnLogin")
btn_login.click()
'''
#Добавление сотрудника
first_menu = driver.find_element_by_id('menu_pim_viewPimModule')
action.move_to_element(first_menu).perform()
second_menu = driver.find_element_by_id('menu_pim_addEmployee')
second_menu.click()
first_name = driver.find_element_by_id('firstName')
first_name.send_keys('Kiril')
last_name = driver.find_element_by_id('lastName')
last_name.send_keys('Kirilov')
time.sleep(2)
btn_save = driver.find_element_by_id('btnSave')
btn_save.click()'''

#удаление сотрудника
first_menu = driver.find_element_by_id('menu_pim_viewPimModule')
action.move_to_element(first_menu).perform()
second_menu = driver.find_element_by_id('menu_pim_viewEmployeeList')
second_menu.click()
search_employee = driver.find_element_by_id('empsearch_employee_name_empName')
search_employee.send_keys('Kiril Kirilov')
search_btn = driver.find_element_by_id('searchBtn')
search_btn.click()
check_box = driver.find_element_by_id('ohrmList_chkSelectAll')
check_box.click()
delete = driver.find_element_by_id('btnDelete')
delete.click()
btn_ok = driver.find_element_by_id('dialogDeleteBtn')
btn_ok.click()
time.sleep(2)
driver.quit()