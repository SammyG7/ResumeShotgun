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
import os 
import time 
import get_links_glassdoor
import get_links_indeed
import menu
from userProfile import *

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
    driver = webdriver.Chrome('./chromedriver')
    '''
    profile = userProfile()
    profile.loadProfile()
    menu.run(profile)
    profile.saveProfile()
    site = profile.getSite()

    ## Get Links From User Specified Website
    if(site == "glassdoor"):
        aggregatedURLs = get_links_glassdoor.getURLs()
    else:
        aggregatedURLs = get_links_indeed.getURLs(driver, profile)
    
    print(f'Job Listings: {aggregatedURLs}')
    print('\n')
    
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
    '''
    driver.close()
    
