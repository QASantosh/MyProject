from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/parul/santoshworkspace/chromedriver_linux64/chromedriver')
driver.get('https://data.grampower.com/hes/')
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='username']").send_keys("parul")
driver.find_element_by_xpath("//input[@name='password']").send_keys("grampower")
#driver.quit()

