from selenium import webdriver
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("http://demo.automationtesting.in/Alerts.html")

time.sleep(10)
msg = driver.find_element_by_class_name('btn-danger').click()
switch_alert = driver.switch_to.alert
alert_text = switch_alert.text
print(alert_text)
if alert_text != 'I am an alert box!':
    print('Test alert failed')
else:
    print('Test alert passed')
switch_alert.accept()
second_window = driver.current_url
time.sleep(5)

driver.execute_script('window.open();')
new_window= driver.window_handles[1]
driver.switch_to.window(new_window)
driver.get(second_window)
time.sleep(5)

with_alert = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
time.sleep(5)
confium_box = driver.find_element_by_class_name('btn-primary').click()
time.sleep(5)
alert = driver.switch_to.alert
alert.dismiss()

driver.execute_script('window.open();')
new_window= driver.window_handles[2]
driver.switch_to.window(new_window)
driver.get(second_window)
time.sleep(5)
with_alert = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
time.sleep(10)
confium_box = driver.find_element_by_class_name('btn-primary').click()
time.sleep(5)
promt = driver.switch_to.alert
promt.send_keys('Ура! Задание выполнено!')
promt.accept()

