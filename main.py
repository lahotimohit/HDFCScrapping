from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name =[]

driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get(url="https://near-me.hdfcbank.com/branch-atm-locator/")
title = driver.find_elements(By.CLASS_NAME, 'outlet-address')
size = len(title)
for item in range(size):
    name.append(title[item].find_element(By.CLASS_NAME, 'info-text').text)

with open('address.txt', mode='w') as file:
    file.write("List of HDFC Bank- \n")
    for item in name:
        file.write(f"{item}\n\n\n")