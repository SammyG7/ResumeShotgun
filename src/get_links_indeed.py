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
from indeed import Indeed

## @brief Opens indeed.com/ and checks if user is logged in, otherwise calls function to auto login.
#  @param driver a Selenium object utilized to navigate the page.
#  @return boolean representing sign in has been prompted or user is already signed in.
def login(driver):
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
    ## Email
    driver.get("https://secure.indeed.com/account/login?hl=en_CA&amp;co=CA&amp;continue=https%3A%2F%2Fca.indeed.com%2Fjobs%3Fq%3Dmaterials%2Bengineer%26l%3DHamilton%252C%2BON%26ts%3D1646004111972%26pts%3D1641679429865%26rq%3D1%26rsIdx%3D1&amp;tmpl=desktop&amp;service=my&amp;from=gnav-util-jobsearch--jasx")
    email = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-3']")
    email.send_keys('3XA3Tester@gmail.com')
    #i-unmask css-157vc5a e8ju0x51
    nextbutton = driver.find_element_by_xpath("//*[@class='i-unmask css-157vc5a e8ju0x51']")
    #nextbutton = driver.find_element_by_xpath("//*[@class='css-157vc5a e8ju0x51']")
    nextbutton.click()
    
    captchaHandler(driver)
    time.sleep(1)

    ## Password
    try:
        password = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-111']")
    except: ## Form number seems to change after captcha
        password = driver.find_element_by_xpath("//*[@id='ifl-InputFormField-116']")
    password.send_keys('3XA3Group5')

    nextbutton = driver.find_element_by_xpath("//*[@class='i-unmask css-157vc5a e8ju0x51']")
    #nextbutton = driver.find_element_by_xpath("//*[@class='css-157vc5a e8ju0x51']")
    nextbutton.click()

    captchaHandler(driver)
    time.sleep(1)
    verificationHandler(driver)

def waitForElement(xpath):
    found = False

    while not found:
        try:
             driver.find_element_by_xpath(xpath)
             found = true
        except:
            time.sleep(1)
            pass

def captchaHandler(driver):
    time.sleep(1)
    detected = False
    try:
        driver.find_element_by_xpath("//*[@class='pass-Captcha css-1lbfmuq eu4oa1w0']")
        print("Captcha Detected: Waiting for user")
        detected = True
        while(True):
            driver.find_element_by_xpath("//*[@class='pass-Captcha css-1lbfmuq eu4oa1w0']")
    except:
        if(detected):
            print("Captcha Cleared")
        return

def verificationHandler(driver):
    try:
        driver.find_element_by_xpath("//*[@id='verification_input']")
        print("Two Step Verification Detected: Waiting for user")
        while(True):
            driver.find_element_by_xpath("//*[@id='verification_input']")
    except:
        return

## @brief Instantiates a Selenium chrome driver with executable path to the chrome driver lcoation then calls login()
def run(driver, profile):
    ## Non Hardcoded Email + Resume
    success = False
    driver.get('https://ca.indeed.com/')
    
    if(profile.getAutoLogin()): # *** Change with working autoLogin
        ## Attempt Auto Login
        print("Attempting Automatic Login")
        try:    
            success = login(driver)
        except:
            print("Something Went Wrong")
            print("Switching to Manual Login")
            pass
    else:
        print("Manual Login Required")

        
        
    ## Manually log in if automatic didn't work
    while(not success):
        ## Periodically check if logged in
        time.sleep(2)
        try: ## Crashes if on wrong page anyways
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            mosaic = soup.find(id='mosaic-data')
            text = mosaic.text.split("\n")

            for x in text:
                if('window.mosaic.providerData["mosaic-provider-serpreportjob"]' in x[:70]):
                    logInCheck = x

            if('"isLoggedIn":true' in logInCheck):
                success = True
        except:
            pass

    print("Logged in")

    linkbot = Indeed(profile.getJobTitle(), profile.getLocation()[0], driver)
    linkbot.run()
    return linkbot.returnLinks()

## Old HTML
# nextbutton = driver.find_element_by_xpath("//*[@class='css-rhczsh e8ju0x51']")
