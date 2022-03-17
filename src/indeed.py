## @file Indeed.py
#  @author Jeremy Langner
#  @brief Module that extracts job posting links from Indeed and returns the job title and company to the user.
#  @date March 17, 2022

import sys
import time
import requests
from unittest import result
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup



#keyword and location from user input module
keyword = ""
location = ""

#global constants
pages = 0
allJobs = []

## @brief Enters in search parameters and returns url of results.
#  @details Uses Selenium to send keys to Indeed.com
#  @param keyword a string representing the job title/poistion that the user is interested in searching for.
#  @param location a string representing the desired job location.
#  @return string representing the url of the search results. 
def search(keyword, location):
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=driverLocation)

    driver.get("https://ca.indeed.com/")
    driver.find_element(By.ID,"text-input-what").send_keys(str(keyword))
    time.sleep(.5)

    driver.find_element(By.ID,"text-input-where").send_keys(Keys.CONTROL + "a")
    driver.find_element(By.ID,"text-input-where").send_keys(Keys.DELETE)
    driver.find_element(By.ID,"text-input-where").send_keys(str(location))
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME,"yosegi-InlineWhatWhere-primaryButton").click()

    
    return driver.current_url

## @brief Traverses through the url to search and save jobs on a single page.
#  @param url a string representing an Indeed url with valid search results.
#  @return list containing tuples of job title and company.
def getJobs(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    cards = soup.find_all("td",class_="resultContent")
    jobs = []
    for card in cards:
        data = card.find_all("span")
        #print(data)
        job = []
        for item in data:
            if item.text not in job and item.text != "new":
                job.append(item.text)
        jobs.append(job[:2])
    print(jobs)

    return jobs


## @brief Gets number of pages based on an Indeed search result.
#  @param url a string representing an Indeed url with valid search results.
#  @return int which represents the numbers of pages of results from such single search.
def getPages(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    totalPages = soup.find("div",id="searchCountPages")

    numJobs = totalPages.text
    flag = False
    temp = ""
    for i in range(len(numJobs)):

        if numJobs[i] == "f" and flag == False:
            flag = True
        elif flag and 48 <= ord(numJobs[i]) <= 57:
            temp += numJobs[i]
    

    pages = int(temp)
    if pages%15 != 0:
        pages = pages//15 + 1

    
    return pages

## @brief Formats various indeed job search pages.
#  @return a string representing the next page.
def pageParser():
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=driverLocation)
    url = "https://ca.indeed.com/jobs?q=Engineer&l=barrie&vjk=f6f5b3957533926a"
    driver.get(url)

    for i in range(getPages("https://ca.indeed.com/jobs?q=Engineer&l=barrie&vjk=f6f5b3957533926a")):
        currUrl = url[:-20] + "start=" + str(i)+ "0"
        
        print(currUrl)
        
    #placeholder return
    return currUrl


if __name__ == "__main__":
    #Search indeed based on a keyword and a location.
    #search(sys.argv[1],sys.argv[2])

    #get jobsed based on a passed url which is added to a list
    #getJobs("https://ca.indeed.com/jobs?q=Engineer&l=Toronto%2CON&vjk=f6f5b3957533926a")

    #Helper method to get the number of pages required
    #getPages("https://ca.indeed.com/jobs?q=Engineer&l=Toronto%2CON&vjk=f6f5b3957533926a")

    #Page parser to traverse indeed website
    #pageParser()
