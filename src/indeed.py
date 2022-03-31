## @file Indeed.py
#  @author Jeremy Langner
#  @brief Module that extracts job posting links from Indeed and returns the job title and company to the user.
#  @date March 17, 2022

import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Job import Job

from bs4 import BeautifulSoup

class Indeed:

    #Search Info
    jobs = []
    links = []
    url = ""
    keyword = ""
    location = ""
    jobPages = 0
    numJobs = 0
    nextPages = []

    #Soup Info
    page = ""
    soup = ""


    ## @brief Constructs a job search using Indeed.
    #  @param keyword a string representing the job title/poistion that the user is interested in searching for.
    #  @param location a string representing the desired job location.
    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location
        self.driverLocation = "./chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.driverLocation)

    def updateCurrentPage(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    ## @brief Enters in search parameters and returns url of results.
    #  @details Uses Selenium to send keys to Indeed.com
    def search(self):
        
        self.driver.get("https://ca.indeed.com/")
        self.driver.find_element(By.ID,"text-input-what").send_keys(self.keyword)
        time.sleep(.5)

        self.driver.find_element(By.ID,"text-input-where").send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.ID,"text-input-where").send_keys(Keys.DELETE)
        self.driver.find_element(By.ID,"text-input-where").send_keys(self.location)
        time.sleep(0.5)
        self.driver.find_element(By.CLASS_NAME,"yosegi-InlineWhatWhere-primaryButton").click()

        self.url = self.driver.current_url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
    
    ## @brief Find essential job info(title, company, link) and creates a Job class
    #  @details Uses beautiful soup to search linearly down the page with two different 
    #  methods but allign once search with the other properly
    def getJob(self):
        
        #find html that contains all table results that contain the job title and company
        infoCards = self.soup.find_all("td",class_="resultContent")

        #find html that contains href data
        div = self.soup.find("div",class_="mosaic-provider-jobcards")
        linkCards = div.find_all("a", href=True, id=True)

        #search through both html list data
        for info,links in zip(infoCards, linkCards):
            j = Job()

            data = info.find_all("span")

            #create a temporary list of a specifc job card's info
            job = []

            #traverse through span elements of ecah job card that contain the job info
            for item in data:
                if item.text not in job and item.text != "new":
                    job.append(item.text)

            j.setTitle(job[0])
            j.setCompany(job[1])

            jobLink = links['href']

            #check that job link is proper format
            if(jobLink[:8] == "/pagead/" or jobLink[:9] == "/company/" or jobLink[:4] == "/rc/"):
                j.setLink("https://ca.indeed.com" + jobLink)

            self.jobs.append(j)

    ## @brief Gets number of pages based on an Indeed search result.
    def getPages(self):
        totalPages = self.soup.find("div",id="searchCountPages")

        numJobs = totalPages.text
        flag = False
        temp = ""
        for i in range(len(numJobs)):

            if numJobs[i] == "f" and flag == False:
                flag = True
            elif flag and 48 <= ord(numJobs[i]) <= 57:
                temp += numJobs[i]
        
        self.numJobs = int(temp)

        pages = self.numJobs//15
        if self.numJobs%15 != 0:
            pages = self.numJobs//15 + 1

        self.jobPages = pages

    ## @brief Formats various indeed job search pages.
    def pageParser(self):

        self.driver.get(self.url)

        if self.url != '':
            self.url = 'https://ca.indeed.com/jobs?q=' + self.keyword +'&l=' + self.location

        for i in range(self.jobPages):
            currUrl = self.url + "&start=" + str(i)+ "0"
            self.nextPages.append(currUrl)

    ## @brief Used to run various module functions.
    def run(self):
        try:
            self.search()
            self.getJob()
            self.getPages()
            self.pageParser()
        except:
            return "An error occured with the search"
    
''' Uncomment to run
if __name__ == "__main__":
    
    s1 = Indeed("Software Engineer", "Barrie")
    s1.run()
    print(len(s1.jobs))
    print(s1.returnLinks())
    #hehe
    #for i in range(len(s1.jobs)):
    #    print([s1.jobs[i].title, s1.jobs[i].company, s1.jobs[i].link])

    #s1.clear()

    #s1.search()
    #s1.getPages()
    #s1.pageParser()  
=======
    s1 = Indeed("Engineer", "Huntsville, ON")
    s1.run()  
'''

