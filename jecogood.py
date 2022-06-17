from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://docs.python.org/3/tutorial/venv.html")
find = driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[12]/div/form/input[1]')
find.send_keys("what now")
button = driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[12]/div/form/input[2]')
button.click()