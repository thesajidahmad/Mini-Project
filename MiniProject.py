import time
#from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import xlrd
from selenium.webdriver.support.wait import WebDriverWait

serv_object = Service(executable_path=r"C:\Users\Sajid\PycharmProjects\sele_test\Driver\geckodriver.exe")

qa = xlrd.open_workbook("mini-project.xls")
sheet = qa.sheet_by_name("Sheet1")

rowcount = sheet.nrows
colcount = sheet.ncols

print(rowcount)
print(colcount)

for curr_row in range(1, rowcount):
    driver = webdriver.Firefox(service=serv_object)
    FName = sheet.cell_value(curr_row, 0)
    MName = sheet.cell_value(curr_row, 1)
    LName = sheet.cell_value(curr_row, 2)
    DOB = sheet.cell_value(curr_row, 3)
    Email = sheet.cell_value(curr_row, 4)
    PasW = sheet.cell_value(curr_row, 5)


#open login page
    driver.get("https://sajid-mini-project.s3.ap-south-1.amazonaws.com/Mini+Project/login.html")
    driver.maximize_window()

    driver.implicitly_wait(180)
    #driver.get("https://sajid-mini-project.s3.ap-south-1.amazonaws.com/Mini+Project/login.html")
    driver.refresh()
    time.sleep(1)

#signup
    driver.find_element(By.XPATH, "//a[@id='reg']").click()
#First_Name
    user = driver.find_element(By.ID, "reg-fname")
    user.click()
    user.send_keys(FName)
#Middle_Name
    user = driver.find_element(By.ID, "reg-mname")
    user.click()
    user.send_keys(MName)
#Last_Name
    user = driver.find_element(By.ID, "reg-lname")
    user.click()
    user.send_keys(LName)
#Date of Birth
    user = driver.find_element(By.ID, "dob")
    user.click()
    user.send_keys(DOB)
#Gender
    driver.find_element(By.ID, "male").click()
    #driver.find_element(By.ID, "female").click()
    #driver.find_element(By.ID, "other").click()
#Course
    driver.find_element(By.XPATH, "//option[contains(text(),'B.Tech')]").click()
#Branch
    driver.find_element(By.XPATH, "//option[contains(text(),'CSE')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'ECE')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'AI & ML')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'CS-IT')]").click()
    #driver.find_element(By.XPATH, "//body/form[1]/fieldset[1]/div[1]/select[2]/option[5]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'ME')]").click()
#Year
    #driver.find_element(By.XPATH, "//option[contains(text(),'2017-21')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2018-22')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2019-23')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2020-24')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2021-25')]").click()
    driver.find_element(By.XPATH, "//option[contains(text(),'2022-26')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2023-27')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2024-28')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2025-29')]").click()
    #driver.find_element(By.XPATH, "//option[contains(text(),'2026-30')]").click()
#Email
    email = driver.find_element(By.ID, "reg-email")
    email.click()
    email.send_keys(Email)
#password
    passw = driver.find_element(By.ID, "reg-pass")
    passw.click()
    passw.send_keys(PasW)
#confirm password
    conpass = driver.find_element(By.ID, "reg-re-pass")
    conpass.click()
    conpass.send_keys(PasW)
#register
    driver.find_element(By.XPATH, "//b[contains(text(),'Register')]").click()
    time.sleep(1)

    driver.close()



