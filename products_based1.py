from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("http://demo.automationtesting.in/Loader.html")

btn_run = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.id('loader')))