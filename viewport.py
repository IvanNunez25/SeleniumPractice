import time

from selenium import webdriver

viewports = [ (1024, 768), (768, 1024), (375, 667), (414, 896) ]

driver = webdriver.Firefox()
driver.get( "https://www.google.com/" )

for width, height in viewports:
    driver.set_window_size( width, height )
    time.sleep( 3 )

driver.quit()