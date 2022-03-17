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
import os # to get the resume file
import time # to sleep
import get_links_glassdoor
import get_links_indeed
import menu
from userProfile import *

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
    "email": "test@test.com",
    "phone": "123-456-7890",
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

## @brief Initial function run upon execution of program
#  @details Gathers links through secondary modules then coordinates the apllication process
if __name__ == '__main__':

    profile = userProfile()
    profile.loadProfile()
    menu.run(profile)
    profile.saveProfile()
    site = profile.getSite()

    ## Get Links From User Specified Website
    if(site == "glassdoor"):
        aggregatedURLs = get_links_glassdoor.getURLs()
    else:
        aggregatedURLs = get_links_indeed.getURLs()
        
    print(f'Job Listings: {aggregatedURLs}')
    print('\n')

    driver = webdriver.Chrome(executable_path='./chromedriver')
    
    for url in aggregatedURLs:
        print('\n')

        ## Decide application process based on URL information
        if 'greenhouse' in url:
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
