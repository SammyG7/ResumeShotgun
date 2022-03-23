## @file get_links_glassdoor.py
#  @author Jeremy Langner
#  @author Sam Gorman
#  @brief Module used for collecting links from the Glassdoor site
#  @date Mar 17, 2022

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

## Global Variables
PREFERENCES = {
    "position_title": "Software Engineer",
    "location": "San Francisco, CA"
}


## @brief Helper method which gives the user time to log into Glassdoor
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
#  @return Boolean value of True to signal that login completed successfully
def login(driver):
    driver.get('https://www.glassdoor.com/index.htm')

    while True:
        try:
            WebDriverWait(driver, 1).until(EC.url_contains("member"))
        except TimeoutException:
            break

    return True

## @brief Navigates to appropriate job listing page
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
#  @return Boolean value to signal if process happened correctly or if an error occurred
def go_to_listings(driver):

    ## Wait for the search bar to appear
    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='scBar']"))
        )

    try:
        ## Look for search bar fields
        position_field = driver.find_element_by_xpath("//*[@id='sc.keyword']")
        location_field = driver.find_element_by_xpath("//*[@id='sc.location']")
        location_field.clear()

        ## Fill in with pre-defined data
        position_field.send_keys(PREFERENCES['position_title'])
        location_field.clear()
        location_field.send_keys(PREFERENCES['location'])

        ## Wait for a little so location gets set
        time.sleep(1)
        driver.find_element_by_xpath(" //*[@id='scBar']/div/button").click()

        ## Close a random popup if it shows up
        try:
            driver.find_element_by_xpath("//*[@id='JAModal']/div/div[2]/span").click()
        except NoSuchElementException:
            pass

        return True

    except NoSuchElementException:
        return False

## @brief Aggregates all url links in a set
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
#  @return Set of strings defining all of the collected and cleaned links
def aggregate_links(driver):
    allLinks = []

    ## Wait for page to fully load
    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='MainCol']/div[1]/ul"))
        )

    time.sleep(5)

    ## Parse the page source using beautiful soup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source)

    ## Find all hrefs
    allJobLinks = soup.findAll("a", {"class": "jobLink"})
    allLinks = [jobLink['href'] for jobLink in allJobLinks]
    allFixedLinks = []

    ## Clean up the job links 
    for link in allLinks:
        link = link.replace("GD_JOB_AD", "GD_JOB_VIEW")

        if link[0] == '/':
            link = f"https://www.glassdoor.com{link}"

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}
        request=urllib.request.Request(link,None,headers) 

        try:
            response = urllib.request.urlopen(request)
            newLink = response.geturl()

            if "glassdoor" not in newLink:
                print(newLink)
                print('\n')
                allFixedLinks.append(newLink)
        except Exception:
            print(f'ERROR: failed for {link}')
            print('\n')

    return set(allFixedLinks)

## @brief Main method of module which coordinates acquisition and handling of links 
#  @return Set of strings defining all of the collected links
def getURLs():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    success = login(driver)
    if not success:
        print("Failure"*20)
        driver.close()

    success = go_to_listings(driver)
    if not success:
        driver.close()

    allLinks = set()
    page = 1
    next_url = ''
    while page < 3:
        print(f'\nNEXT PAGE #: {page}\n')

        if page == 1:
            allLinks.update(aggregate_links(driver))

            next_page = driver.find_element_by_xpath("//*[@id='FooterPageNav']/div/ul/li[3]/a")
            this_page = next_page.get_attribute('href')

            m = re.search('(?P<url>[^;]*?)(?P<page>.htm\?p=)(?P<pagenum>.)', this_page)

            page += 1 
            next_url = f"{m.group('url')}_IP{page}.htm" 
            time.sleep(1)

        if page >=2 :
            driver.get(next_url)
            allLinks.update(aggregate_links(driver))
            m = re.search('(?P<url>[^;]*?)(?P<pagenum>.)(?P<html>.htm)', next_url)
            page += 1
            next_url = f"{m.group('url')}{page}.htm"

    driver.close()
    return allLinks
