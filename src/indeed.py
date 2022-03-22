import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

    #Selenium Driver Info
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=driverLocation)

    ## @brief Constructs a job search using Indeed.
    #  @param keyword a string representing the job title/poistion that the user is interested in searching for.
    #  @param location a string representing the desired job location.
    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location

    def getItems(self):
        return self.jobs.items()

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

    
    def getJobs(self):
        
        cards = self.soup.find_all("td",class_="resultContent")

        #search through job cards
        for card in cards:
            data = card.find_all("span")
            #print(data)
            job = []

            #traverse through span elements of ecah job card that contain the job info
            for item in data:
                if item.text not in job and item.text != "new":
                    job.append(item.text)
            self.jobs.append(job[:2])

    ## @brief Traverses through the url to search and save jobs on a single page.
    def getUrls(self):

        div = self.soup.find("div",class_="mosaic-provider-jobcards")
        cards = div.find_all("a", href=True)

        for card in cards:
            jobLink = card['href']
            if(jobLink[:8] == "/pagead/" or jobLink[:9] == "/company/" or jobLink[:4] == "/rc/"):
                self.links.append("https://ca.indeed.com" + jobLink)

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

    def pageParser(self):

        self.driver.get(self.url)

        if self.url != '':
            self.url = 'https://ca.indeed.com/jobs?q=' + self.keyword +'&l=' + self.location

        for i in range(self.jobPages):
            currUrl = self.url + "&start=" + str(i)+ "0"
            self.nextPages.append(currUrl)

    def run(self):
        try:
            self.search()
            self.getJobs()
            self.getUrls()
            self.getPages()
            self.pageParser()
            for i in range(len(self.nextPages)):
                self.updateCurrentPage(self.nextPages[i])
                self.getJobs()
            print(self.jobs)
            print(len(self.jobs))
        except:
            return "An error occured with the search"
    
    
if __name__ == "__main__":
    s1 = Indeed("Engineer", "Collingwood")
    s1.run()