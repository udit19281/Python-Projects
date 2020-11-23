from selenium import webdriver
from time import sleep

driver=webdriver.Chrome("C:\\Chromedriver") #update chrome driver path
driver.get("https://web.whatsapp.com/")

print("[+] ENTER DETAILS AFTER SCANNING FROM THE WEB :)")

us=input("[+] USERNAME:  ")
mes=input("[+] ENTER MESSAGE TO BE SENT: ")
C=int(input("[+] NUMBER OF MESSAGES TO BE SENT: "))
driver.find_element_by_xpath('//span[@title= "{}" ]'.format(us)).click()
x=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
for i in range(C):
     x.send_keys(mes)
     driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
     print("[+] count :" + str(i+1))
