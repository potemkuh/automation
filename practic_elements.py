from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/l")
action = ActionChains(driver)

#Авторизация
login = driver.find_element_by_id("txtUsername")
login.send_keys('Admin')
password = driver.find_element_by_id("txtPassword")
password.send_keys('admin123')
btn_login = driver.find_element_by_id("btnLogin").click()
driver.set_script_timeout(5)

#Переход к employee list
first_menu = driver.find_element_by_id('menu_pim_viewPimModule')
action.move_to_element(first_menu).perform()
second_menu = driver.find_element_by_id('menu_pim_viewEmployeeList').click()
emplyoee = driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[1]/td[3]/a').click()

#проверка чек-бокса Gender на доступность
gender = driver.find_element_by_xpath('//*[@id="personal_optGender_2"]')
check_gender = gender.get_attribute("disabled")
if check_gender:
    print("Изменить пол нельзя")
else:
    print("можно изменить пол")

#проверка селекта Nationality на доступность
el_select = driver.find_element_by_id('personal_cmbNation')
check_select = el_select.get_attribute("disabled")
if check_gender:
    print("Изменить национальность нельзя")
else:
    print("можно изменить национальность")

#переход к изменению сотрудника
btn_edit = driver.find_element_by_id('btnSave').click()

#Переключение чек-бокса Gender и проверка включения
chek_on = driver.find_element_by_id('personal_optGender_2').click()
check = driver.find_element_by_id('personal_optGender_2')
edit_check = check.get_attribute("checked")
if edit_check is not None:
    print("Чекбокс отмечен")
else:
    print("Чекбокс не отмечен")
nationality = driver.find_element_by_id('personal_cmbNation')
select = Select(nationality)
select.select_by_value('193')

save = driver.find_element_by_id('btnSave').click()
driver.quit()