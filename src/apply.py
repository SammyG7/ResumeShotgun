## @file apply.py
#  @author Gavin Jameson
#  @author Jeremy Langner
#  @author Sam Gorman
#  @brief Main module used for the application proccess
#  @date Mar 17, 2022

## Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import time 
import get_links_glassdoor
import get_links_indeed
import menu
from userProfile import *
from bs4 import BeautifulSoup
import requests
import random

from pdfReader import pdfReader ##*****Temp

## Global Variables
URL_l2 = 'https://jobs.lever.co/scratch/2f09a461-f01d-4041-a369-c64c1887ed97/apply?lever-source=Glassdoor'
URL_l3 = 'https://jobs.lever.co/fleetsmith/eb6648a6-7ad9-4f4a-9918-8b124e10c525/apply?lever-source=Glassdoor'
URL_l4 = 'https://jobs.lever.co/stellar/0e5a506b-1964-40b4-93ab-31a1ee4e4f90/apply?lever-source=Glassdoor'
URL_l6 = 'https://jobs.lever.co/verkada/29c66147-82ef-4293-9a6a-aeed7e6d619e/apply?lever-source=Glassdoor'
URL_l8 = 'https://jobs.lever.co/rimeto/bdca896f-e7e7-4f27-a894-41b47c729c63/apply?lever-source=Glassdoor'
URL_l9 = 'https://jobs.lever.co/color/20ea56b8-fed2-413c-982d-6173e336d51c/apply?lever-source=Glassdoor'
URL_g1 = 'https://boards.greenhouse.io/instabase/jobs/4729606002?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'

URLS = [URL_g1, URL_l4, URL_l3, URL_l6, URL_l8, URL_l9]

JOB_APP = {
    "first_name": "Foo",
    "last_name": "Bar",
    "email": "3XA3Tester@gmail.com",
    "phone": "9053872700",
    "org": "Self-Employed",
    "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/",
    "website": "www.youtube.com",
    "github": "https://github.com",
    "twitter": "www.twitter.com",
    "location": "San Francisco, California, United States",
    "grad_month": '06',
    "grad_year": '2021',
    "university": "MIT"
}

## @brief Fills in website text boxes with user information and submits resume
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def greenhouse(driver):

    ## Fill Basic Info
    driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    driver.find_element_by_id('email').send_keys(JOB_APP['email'])
    driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        time.sleep(2) 

    except NoSuchElementException:
        pass

    ## Upload Resume as a Text File
    driver.find_element_by_css_selector("[data-source='paste']").click()
    resume_zone = driver.find_element_by_id('resume_text')
    resume_zone.click()
    with open(JOB_APP['resume_textfile']) as f:
        lines = f.readlines() # add each line of resume to the text area
        for line in lines:
            resume_zone.send_keys(line.decode('utf-8'))

    ## Fill Additional Info
    try:
        driver.find_element_by_xpath("//label[contains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//label[contains(.,'Linkedin')]").send_keys(JOB_APP['linkedin'])
        except NoSuchElementException:
            pass

    try:
        driver.find_element_by_xpath("//select/option[text()='2021']").click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Harvard')]").click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_xpath("//label[contains(.,'Website')]").send_keys(JOB_APP['website'])
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    except NoSuchElementException:
        pass

    ## Submit Resume
    driver.find_element_by_id("submit_app").click()

## @brief Fills in website text boxes with user information and submits resume
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def lever(driver):
    ## Navigate to the application page
    driver.find_element_by_class_name('template-btn-submit').click()

    ## Fill Basic Info
    first_name = JOB_APP['first_name']
    last_name = JOB_APP['last_name']
    full_name = first_name + ' ' + last_name
    driver.find_element_by_name('name').send_keys(full_name)
    driver.find_element_by_name('email').send_keys(JOB_APP['email'])
    driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
    driver.find_element_by_name('org').send_keys(JOB_APP['org'])

    driver.find_element_by_name('urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
    driver.find_element_by_name('urls[Twitter]').send_keys(JOB_APP['twitter'])
    try: 
        driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name('urls[GitHub]').send_keys(JOB_APP['github'])
        except NoSuchElementException:
            pass
    driver.find_element_by_name('urls[Portfolio]').send_keys(JOB_APP['website'])

    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(JOB_APP['university'])
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath("//select/option[text()='Glassdoor']").click()
    except NoSuchElementException:
        pass

    ## Submit Resume
    driver.find_element_by_name('resume').send_keys(os.getcwd()+"/resume.pdf")
    driver.find_element_by_class_name('template-btn-submit').click()

## @brief Ensures that the job page support an application through indeed then initiates the applicaiton process
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def indeed(driver):

    page = requests.get(driver.current_url)
 
    soup = BeautifulSoup(page.content, "html.parser")

    applyBtn = soup.find("span", class_="jobsearch-IndeedApplyButton-newDesign")
    
    if applyBtn.text != "Apply now":
        #print("Error! Cannot apply on indeed")
        return ValueError("Error! Cannot apply on indeed")
    else:
        driver.find_element(By.XPATH, "//*[@id='indeedApplyButton']").click()
        #print("worked")
    time.sleep(round(random.uniform(0.1,0.75), 4))

    runApplication(driver)
        

## @brief Main method to execute to traverse indeed application process
#  @detail Creates a dict to store the different steps of an indeed applicaiotn process which are usually not in order. Then the module determines which step is at and applies the automatic applicaiotn for such step
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def runApplication(driver):

    # dictionary of application step to corresponding function
    pages = {
        "contact-info": contactInfo,
        "resume": selectResume,
        "work-experience": pastJob,
        "documents": coverLetter,
        "review": reviewApp,
    }

    '''
    Typical indeed questions:
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
    for _ in range(numSteps):
        header = getHeader(driver)
        print(header)
        try:
            #check if header is in the dicitonary of possible pages
            if header in pages:
                pages[header](driver)
            else:
                manual(driver)
        except:
            print("yikes")
            return ValueError("Overall function broke")
        time.sleep(1)

## @brief Function that gets the application step based on the url
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
#  @return header of type string of the header keyword that summarizes what the step needs
def getHeader(driver):
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))

    link = driver.current_url
    header = ""
    for char in reversed(link):
        if char == "/":
            break
        else:
            header = char + header

    return header

## @brief Function that handles user contact info submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def contactInfo(driver):

    try:        
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
    except:
        print("Error on contact info")
        return ValueError

## @brief Function that handles user manual info submission and interaction with user
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def manual(driver):
    # Lets user know they need to add info then requests them to press Enter!
    print("Please fill out form on the open google chrome tab then press Enter!")
    inp = input()
    if inp == "":
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();

## @brief Function that handles user resume selection page submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def selectResume(driver):

    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='resume-display-buttonHeader']/div[2]/span[1]")))
        element.click();

        element2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element2.click();
    except:
        print("Error on resume")
        return ValueError

## @brief Function that handles past job experience submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def pastJob(driver):
    
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
    except:
        print("Error on upload past job exp")
        return ValueError

## @brief Function that handles user cover letter submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def coverLetter(driver):
    
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
    except:
        print("Error on cover letter upload")
        return ValueError

## @brief Function that handles user final user info submission and application
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def reviewApp(driver):
    try:
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        print("Not submitting final submission")
        return
    except:
        return ValueError("Error on final submission")


## @brief Initial function run upon execution of program
#  @details Gathers links through secondary modules then coordinates the apllication process
if __name__ == '__main__':
    '''
    ## PDF Tests. Just delete if you're working in apply
    resume = pdfReader("./Resumes/BobBobberResume.pdf")
    '''

    profile = userProfile()
    profile.loadProfile()
    menu.run(profile)
    profile.saveProfile()
 

    site = profile.getSite()
    #site = ""                   ##-----

    #path = './chromedriver'
    #servicePath = Service(path) 
    #driver = webdriver.Chrome("/usr/bin/chromedriver") # Jeremy's path
    driver = webdriver.Chrome("./chromedriver") 
    
    #aggregatedURLs = get_links_indeed.run(driver, profile)
    
    #driver.close()

    '''
    for link in aggregatedURLs:
        ##indeed(driver.get(link))
        print(link)
        print("\n")
    

    ##print(len(aggregatedURLs))

    
    profile = userProfile()
    profile.loadProfile()
    menu.run(profile)
    profile.saveProfile()
    site = profile.getSite()
    '''
    

    ## Get Links From User Specified Website
    if(site == "glassdoor"):
        aggregatedURLs = get_links_glassdoor.getURLs()
    else:
        aggregatedURLs = get_links_indeed.run(driver, profile)
    
        
    #print(f'Job Listings: {aggregatedURLs}')
    print(f'Job Listings:')
    print('\n')
    
    for url in aggregatedURLs:
        print('\n')
        #indeed(driver.get(link))

        ## Decide application process based on URL information
        if 'indeed' in url:
            print("Indeed\n")
            print("URL: ", url)
            driver.get(url)
            try:
                driver.switch_to.alert.accept()
            except:
                pass

            try:
                indeed(driver)
                print(f'SUCCESS FOR: {url}')
            except:
                print(f"Apply manually for: {url}")
            
        elif 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                continue
            
        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                continue
        else:
            continue

        time.sleep(1)
    

    driver.close()
    
