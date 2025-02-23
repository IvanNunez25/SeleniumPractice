import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get( "https://fs2.formsite.com/meherpavan/form2/index.html" )

driver.maximize_window()
driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );" )

'''
driver.find_element( By.XPATH, "//label[@for='RESULT_CheckBox-8_0']" ).click()
time.sleep( 5 )
driver.find_element( By.XPATH, "//label[@for='RESULT_CheckBox-8_0']" ).click()
'''

checkboxes = driver.find_elements( By.XPATH, "//input[@type='checkbox']" )

for checkbox in checkboxes:
    checkbox.send_keys( Keys.SPACE )

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expexted_checked_count = 7

if checked_count == expexted_checked_count:
    print( 'Checkbox count verified' )
else:
    print( 'Checkbox count mismatch' )

time.sleep( 3 )
driver.close()


