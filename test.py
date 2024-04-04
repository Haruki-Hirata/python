#encoding='UTF-8'

!pip install selenium
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://cmps-web.oka-pu.ac.jp/campusweb/')



elem_username = browser.find_element_by_id('username')
elem_username.send_keys('se319033')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('Qb5miPVjq2W')

elem_login_btn = browser.find_element_by_name('_eventId_proceed')
elem_login_btn.click()
elem_login_btn = browser.find_element_by_name('_eventId_proceed')
elem_login_btn.click()

elem_class = browser.find_element_by_class_name('kaiko')

#encoding='UTF-8'
f = open('間割.csv','w')
f.write(str(elem_class.text))
f.close()

kanwari = r'C:\Users\Owner\docker-python\test2.py\間割.csv'

import subprocess
subprocess.Popen(["start",kanwari], shell=True,)

pyinstaller --onefile test.py

