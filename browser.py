import time
from itertools import dropwhile
from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get( "https://opensource-demo.orangehrmlive.com/" )
driver.maximize_window()
time.sleep( 3 )
#driver.minimize_window()
#driver.fullscreen_window()
link = driver.find_element( By.CSS_SELECTOR, '.oxd-text.oxd-text--p.orangehrm-login-forgot-header' )
time.sleep( 3 )
link.click()
time.sleep(3)

driver.back()
time.sleep( 3 )
driver.forward()
time.sleep( 3 )
driver.refresh()
driver.close()