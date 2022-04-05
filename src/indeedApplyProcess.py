## @file indeedApplyProcess.py
#  @author Gavin Jameson
#  @author Jeremy Langner
#  @author Sam Gorman
#  @brief Main module used for the application proccess
#  @date Mar 17, 2022

## Imports
from gettext import find
from multiprocessing.managers import ValueProxy
import numbers
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

    # dictionary of header values to corresponding function
    '''
    pages = {
        "Add your contact information":contactInfo,
        "Questions from": manual,
        "Add a resume": selectResume,
        "Select a past job that shows relevant experience": pastJob,
        "Want to include any supporting documents?": coverLetter,
        "Please review your application": reviewApp,
    }
    
    '''
    pages = {
        1:contactInfo,
        2: manual,
        3: selectResume,
        4: pastJob,
        5: coverLetter,
        6: reviewApp,
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
    numSteps = int((driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[1]/div/div[2]/div[2]").text)[-1])

    # Go through all application steps

    contactInfo(driver)
    selectResume(driver)
    coverLetter(driver)

    '''
    for _ in range(numSteps):
        header = str(driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/h1").text)
        print(header)
        try:
            #check if header is in the dicitonary of possible pages
            if "contact information" in header:
                contactInfo(driver)
            elif "Questions" in header:
                manual(driver)
            elif "resume" in header:
                selectResume(driver)
            elif "past job" in header:
                pastJob(driver)
            elif "supporting documents" in header:
                coverLetter(driver)
            elif "review your application" in header:
                reviewApp(driver)
            else:
                manual(driver)
        except:
            print("yikes")
            return ValueError("Overall function broke")
    '''

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

    except:
        return ValueError("Error on information page input")

def manual(driver):
    # Lets user know they need to add info then requests them to press Enter!
    print("Please fill out form on the open google chrome tab then press Enter!")
    inp = input()
    if inp == "":
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()

def selectResume(driver):

    try:
        driver.find_element(By.XPATH, "//*[@id='resume-display-buttonHeader']/div[2]/span[1]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
    except:
        return ValueError("Error on resume upload page")


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
    except:
        return ValueError("Error on cover letter upload")

def reviewApp(driver):
    try:
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        pass
    except:
        return ValueError("Error on final submission")

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    url = "https://ca.indeed.com/viewjob?cmp=C.-F.-Crozier-%26-Associates&t=Transportation%20Engineer&jk=0eb2bd1324d739a7&q=engineer&vjs=3"
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='indeedApplyButton']/div").click()
    while driver.current_url != "https://m5.apply.indeed.com/beta/indeedapply/form/contact-info":
        continue

    runApplication(driver)
    #driver.get(url)
