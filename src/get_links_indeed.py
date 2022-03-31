## @file get_links_indeed.py
#  @author Samuel Gorman
#  @brief Module that signs into Indeed website.
#  @date March 17, 2022

## Imports
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
from indeed import *

## @brief Opens indeed.com/ and checks if user is logged in, otherwise calls function to auto login.
#  @param driver a Selenium object utilized to navigate the page.
#  @return boolean representing sign in has been prompted or user is already signed in.
def login(driver):
    driver.get('https://ca.indeed.com/')
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    mosaic = soup.find(id='mosaic-data')
    text = mosaic.text.split("\n")

    for x in text:
        if('window.mosaic.providerData["mosaic-provider-serpreportjob"]' in x[:70]):
            logInCheck = x

    if('"isLoggedIn":false' in logInCheck):
        navigateToLogin(driver)

    return True

## @brief Opens Indeed login page and inputs email and password then signs in.
#  @param driver a Selenium object utilized to navigate the page.
def navigateToLogin(driver):
    driver.get("https://secure.indeed.com/account/login?hl=en_CA&amp;co=CA&amp;continue=https%3A%2F%2Fca.indeed.com%2Fjobs%3Fq%3Dmaterials%2Bengineer%26l%3DHamilton%252C%2BON%26ts%3D1646004111972%26pts%3D1641679429865%26rq%3D1%26rsIdx%3D1&amp;tmpl=desktop&amp;service=my&amp;from=gnav-util-jobsearch--jasx")
    email = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-3']")
    email.send_keys('3XA3Tester@gmail.com')
    #nextbutton = driver.find_element_by_xpath("//*[@class='css-rhczsh e8ju0x51']")
    nextbutton = driver.find_element_by_xpath("//*[@class='css-157vc5a e8ju0x51']")
    # css-157vc5a e8ju0x51
    nextbutton.click()
    time.sleep(1)
    password = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-111']")
    password.send_keys('3XA3Group5')
    nextbutton = driver.find_element_by_xpath("//*[@class='css-rhczsh e8ju0x51']")
    nextbutton.click()

## @brief Instantiates a Selenium chrome driver with executable path to the chrome driver lcoation then calls login()
def run(driver, profile):
    '''
    ## Check for login info
    if(profile.getAutoLogin()):
        success = login(driver)
    '''
    driver.get('https://ca.indeed.com/')
    time.sleep(60)
    print("Hello")
    linkbot = Indeed("engineer", "collingwood", driver)
    linkbot.run()
    return linkbot.returnLinks()
    # time.sleep(100)

#run(webdriver.Chrome('./chromedriver'), 1)
#//*[@id="jobsearch-ViewJobButtons-container"]/div[2]/div/div/span/div[1]/button
#//*[@id="jobsearch-ViewJobButtons-container"]/div[2]/div/div/span/div[1]/button/div


    

