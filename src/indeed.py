## @file Indeed.py
#  @author Jeremy Langner
#  @brief Module that extracts job posting links from Indeed and returns the job title and company to the user.
#  @date March 17, 2022

<<<<<<< HEAD
=======

>>>>>>> Jeremy
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
    ids = []
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
        self.driverLocation = "/usr/bin/chromedriver"
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

<<<<<<< HEAD
## @brief Enters in search parameters and returns url of results.
#  @details Uses Selenium to send keys to Indeed.com
#  @param keyword a string representing the job title/poistion that the user is interested in searching for.
#  @param location a string representing the desired job location.
#  @return string representing the url of the search results. 
def search(keyword, location):
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=driverLocation)
=======
        #search through both html list data
        for info,links in zip(infoCards, linkCards):
            j = Job()

            data = info.find_all("span")
>>>>>>> Jeremy

            #create a temporary list of a specif cjob card's info
            job = []

            #traverse through span elements of ecah job card that contain the job info
            for item in data:
                if item.text not in job and item.text != "new":
                    job.append(item.text)
            j.setTitle(job[0])
            j.setCompany(job[1])

            jobLink = links['href']

<<<<<<< HEAD
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
    
=======
            #check that job link is proper format
            if(jobLink[:8] == "/pagead/" or jobLink[:9] == "/company/" or jobLink[:4] == "/rc/"):
                j.setLink("https://ca.indeed.com" + jobLink)

            j.setTitle(job[0])
            j.setCompany(job[1])
>>>>>>> Jeremy

            self.jobs.append(j)

    ## @brief Gets number of pages based on an Indeed search result.
    def getPages(self):
        totalPages = self.soup.find("div",id="searchCountPages")

<<<<<<< HEAD
## @brief Formats various indeed job search pages.
#  @return a string representing the next page.
def pageParser():
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=driverLocation)
    url = "https://ca.indeed.com/jobs?q=Engineer&l=barrie&vjk=f6f5b3957533926a"
    driver.get(url)
=======
        numJobs = totalPages.text
        flag = False
        temp = ""
        for i in range(len(numJobs)):
>>>>>>> Jeremy

            if numJobs[i] == "f" and flag == False:
                flag = True
            elif flag and 48 <= ord(numJobs[i]) <= 57:
                temp += numJobs[i]
        
<<<<<<< HEAD
    #placeholder return
    return currUrl


=======
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
            #self.getUrls()
            self.getPages()
            self.pageParser()
            
            for i in range(1,len(self.nextPages)):
                self.updateCurrentPage(self.nextPages[i])
                self.getJob()
            #print(self.jobs)
            print(len(self.jobs))
            j = 0
            for i in range(len(self.jobs)):
                print([self.jobs[i].title, self.jobs[i].link])
                j += 1
            print(j)
            #print(self.links)
            #print(self.ids)
        except:
            return "An error occured with the search"
    
    
>>>>>>> Jeremy
if __name__ == "__main__":
    
    s1 = Indeed("Engineer", "Huntsville, ON")
    s1.run()  