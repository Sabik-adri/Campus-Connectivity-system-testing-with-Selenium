import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def thread_sleep(milliseconds):
    time.sleep(milliseconds / 1000)

# Open the Chrome browser
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("http://127.0.0.1:5002/login")

# Maximize the window
driver.maximize_window()
thread_sleep(2000)

# Enter the username
driver.find_element(By.ID, "username").send_keys("admin")
thread_sleep(1000)

# Enter the password
driver.find_element(By.NAME, "password").send_keys("1111")
thread_sleep(1000)

# Click the submit button
driver.find_element(By.ID, "submit").click()
thread_sleep(1000)

driver.find_element(By.ID, "student").click()
thread_sleep(3000)

driver.find_element(By.NAME, "name").send_keys("Plabon Hasan")
thread_sleep(1000)

driver.find_element(By.NAME, "parent").send_keys("Tazul Islam")
thread_sleep(1000)

driver.find_element(By.NAME, "course").send_keys("CSE430")
thread_sleep(3000)

driver.find_element(By.NAME, "section").send_keys("1")
thread_sleep(1000)

driver.find_element(By.NAME, "id").send_keys("2018-2-60-082")
thread_sleep(1000)

driver.find_element(By.NAME, "birthdate").send_keys("08/01/1998")
thread_sleep(1000)

driver.find_element(By.NAME, "gender").send_keys("Male")
thread_sleep(1000)

driver.find_element(By.NAME, "address").send_keys("Dhaka")
thread_sleep(1000)

driver.find_element(By.NAME, "phone").send_keys("01700000000")
thread_sleep(1000)

driver.find_element(By.NAME, "email").send_keys("plabon@gmail.com")
thread_sleep(1000)

driver.find_element(By.ID, "clickStudent").click()
thread_sleep(3000)

driver.find_element(By.ID, "teacher1").click()
thread_sleep(1000)

driver.find_element(By.ID, "addTeacher").click()
thread_sleep(1000)

driver.find_element(By.ID, "add-button").click()
thread_sleep(1000)

driver.find_element(By.ID, "name1").send_keys("Dr. Shamim H Ripon")
thread_sleep(1000)

driver.find_element(By.ID, "reco").send_keys("Professor")
thread_sleep(1000)

driver.find_element(By.ID, "id1").send_keys("456465")
thread_sleep(1000)

driver.find_element(By.ID, "birthdate1").send_keys("01/01/1970")
thread_sleep(1000)

driver.find_element(By.ID, "gender1").send_keys("male")
thread_sleep(1000)

driver.find_element(By.ID, "address1").send_keys("Dhaka")
thread_sleep(1000)

driver.find_element(By.ID, "phone1").send_keys("01711111111")
thread_sleep(1000)

driver.find_element(By.ID, "email1").send_keys("dshr@gmail.com")
thread_sleep(1000)

driver.find_element(By.ID, "addTeacher1").click()
thread_sleep(1000)



# Assuming you expect a message after clicking the submit button
message_element = driver.find_element(By.ID, "message")
if message_element.is_displayed():
    print("Message displayed: " + message_element.text)
else:
    print("Message not found!")

thread_sleep(3000)




# Close the window
driver.quit()
