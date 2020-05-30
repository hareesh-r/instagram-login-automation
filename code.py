from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
"""
save this file with .py extension and run in your pc change the username and password 

to the desired username and password that you want to login
"""

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.instagram.com/')

driver.implicitly_wait(15)

login=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')

login.send_keys('username here')

password=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')

password.send_keys('password here')

loginbutton=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')

loginbutton.click()
