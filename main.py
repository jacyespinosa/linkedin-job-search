from selenium import webdriver
import time


EMAIL = "ENTER EMAIL ADDRESS"
PASSWORD = "ENTER PASSWORD"


chrome_driver_path = "ENTER CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#UPDATE THE LINK TO YOUR OWN PREFERENCE
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=106233382&keywords=software%20engineer&location=San%20Jose%2C%20California%2C%20United%20States")

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


job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in job_list:
    job.click()
    time.sleep(2)

    save_button = driver.find_element_by_css_selector(".jobs-save-button")
    save_button.click()

    time.sleep(5)