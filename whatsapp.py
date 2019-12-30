from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("E:\\work\\workshop\\whatsapp\\chromedriver")

driver.get("https://web.whatsapp.com/")


name=input("Enter the name of person or group: ")
msg=input("Enter a message: ")
count=eval(input("How many times: "))


user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name("_13mgZ")#  _1N6pS 
for i in range(count):
    msg_box.send_keys(msg)
    button=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3M-N-')))#_35EW6
    button.click()
