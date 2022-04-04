## @file indeedApplyProcess.py
#  @author Gavin Jameson
#  @author Jeremy Langner
#  @author Sam Gorman
#  @brief Main module used for the application proccess
#  @date Mar 17, 2022

## Imports
from gettext import find
from multiprocessing.managers import ValueProxy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
#import menu
from bs4 import BeautifulSoup
import requests
import random

def runApplication(driver):
    page = requests.get(driver.current_url)
    soup = BeautifulSoup(page.content, "html.parser")

    pages = {
        "contact information":contactInfo,
        "Questions from the employer": manual,
        "Add a resume for the employer": selectResume,
        "Select a past job that shows relevant experience": pastJob,
        "Want to include any supporting documents?": coverLetter,
        "Please review your application": reviewApp,
    }

    '''
    Typical indeed questions in order:
    Contact Information
    Potential employer questions (experience, job interview times)
    Resume
    Relevant Info(optional)
    Cover Letter(Optional)
    Review
    '''
    #get number of application steps
    numSteps = int(soup.find("div", class_="ia-Navigation-steps").text[-1])

    for i in range(numSteps):
        header = soup.find("h1", class_="ia-BasePage-heading").text

        if header in pages:
            driver = pages[header](driver)
        else:
            driver = manual(driver)

    return 0

def contactInfo(driver):
    page = requests.get(driver.current_url)
 
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        inpFirstName = soup.find("input", id="input-firstName")['value']
        if inpFirstName == "":
            firstNameInput = driver.find_element(By.XPATH, "//*[@id='input-firstName']")
            firstNameInput.send_keys("Foo") #FIRST NAME
        
        inpLastName = soup.find("input", id="input-lastName")['value']
        if inpLastName == "":
            lastNameInput = driver.find_element(By.XPATH, "//*[@id='input-lastName']")
            lastNameInput.send_keys("Bar") #LAST NAME

        inpPhone = soup.find("input", id="input-phoneNumber")['value']
        if inpPhone == "":
            phoneInput = driver.find_element(By.XPATH, "//*[@id='input-phoneNumber']")
            phoneInput.send_keys("905 387 2700") #PHONE NUM
        
        time.sleep(round(random.uniform(0.1,0.75), 4))
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        time.sleep(round(random.uniform(0.1,0.75), 4))
        return driver

    except:
        return ValueError("Error on information page input")

def manual(driver):

    return

def selectResume(driver):

    try:
        driver.find_element(By.XPATH, "//*[@id='resume-display-buttonHeader']/div[2]/span[1]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        return driver
    except:
        return ValueError("Error on resume upload page")

    return 

def pastJob(driver):
    
    try:
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div/div/div/div[1]/span[1]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        return driver
    except:
        return ValueError("Error on job experience page")

def coverLetter(driver):
    
    try:
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/span[1]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button/span").click()
        return driver
    except:
        return ValueError("Error on cover letter upload")

def reviewApp(driver):
    try:
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        return driver
    except:
        return ValueError("Error on final submission")
