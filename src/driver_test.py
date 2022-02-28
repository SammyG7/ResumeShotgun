from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json
import urllib.request
import re
import time 

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://ca.indeed.com/')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

#print(soup.prettify())

#print (soup.find(id='mosaic-data'))

mosaic = soup.find(id='mosaic-data')
#print(mosaic.text)
#print(mosaic.findAll("a", {"class": "jobLink"}))
#print(mosaic.attrs)
text = mosaic.text.split("\n")
##for x in text:
##    print(x[:70])
##    print("--"*20)

for x in text:
    if('window.mosaic.providerData["mosaic-provider-serpreportjob"]' in x[:70]):
        logInCheck = x

    #window.mosaic.providerData["mosaic-provider-serpreportjob"]
if('"isLoggedIn":false' in logInCheck):
        #go_to_Signin()
        driver.get("https://secure.indeed.com/account/login?hl=en_CA&amp;co=CA&amp;continue=https%3A%2F%2Fca.indeed.com%2Fjobs%3Fq%3Dmaterials%2Bengineer%26l%3DHamilton%252C%2BON%26ts%3D1646004111972%26pts%3D1641679429865%26rq%3D1%26rsIdx%3D1&amp;tmpl=desktop&amp;service=my&amp;from=gnav-util-jobsearch--jasx")
        email = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-3']")
        email.send_keys('3XA3Tester@gmail.com')
        nextbutton = driver.find_element_by_xpath("//*[@class='css-rhczsh e8ju0x51']")
        nextbutton.click()
        time.sleep(1)
        password = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-111']")
        password.send_keys('3XA3Group5')
        nextbutton = driver.find_element_by_xpath("//*[@class='css-rhczsh e8ju0x51']")
        nextbutton.click()
        
##        goog = driver.find_element_by_xpath("//*[@id='login-google-button']")
##        goog.click()
        #email = driver.find_element_by_xpath("//*[@id='identifierId']")
##        for winHandle in driver.getWindowHandles():
##            #for x in logInCheck:
##            #driver.switchTo().window(winHandle);
##            print(winHandle)
            

print("Done")
#https://secure.indeed.com/account/login?hl=en_CA&amp;co=CA&amp;continue=https%3A%2F%2Fca.indeed.com%2Fjobs%3Fq%3Dmaterials%2Bengineer%26l%3DHamilton%252C%2BON%26ts%3D1646004111972%26pts%3D1641679429865%26rq%3D1%26rsIdx%3D1&amp;tmpl=desktop&amp;service=my&amp;from=gnav-util-jobsearch--jasx
