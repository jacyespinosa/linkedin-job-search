from selenium import webdriver
import time


EMAIL = "ENTER EMAIL ADDRESS"
PASSWORD = "ENTER PASSWORD"


chrome_driver_path = "ENTER CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

#SIGN IN
time.sleep(5)
sign_in = driver.find_element_by_class_name('cta-modal__primary-btn')
sign_in.click()

username = driver.find_element_by_id('username')
username.send_keys(f'{EMAIL}')

password = driver.find_element_by_id('password')
password.send_keys(f'{PASSWORD}')

sign_in_button = driver.find_element_by_class_name('login__form_action_container ')
sign_in_button.click()
