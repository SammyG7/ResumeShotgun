## @file indeedApplyProcess.py
#  @author Gavin Jameson
#  @author Jeremy Langner
#  @author Sam Gorman
#  @brief Helper module that handles a typical indeed applicaiton process
#  @date April 5, 2022

## Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

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
        #time.sleep(1)
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        #time.sleep(1)
    except:
        print("Error on contact info")
        return -1

## @brief Function that handles user manual info submission and interaction with user
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def manual(driver):
    # Lets user know they need to add info then requests them to press Enter!
    print("Please fill out form on the open google chrome tab then press Enter!")
    inp = input()
    if inp == "":
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        #time.sleep(1)

## @brief Function that handles user resume selection page submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def selectResume(driver):

    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='resume-display-buttonHeader']/div[2]/span[1]")))
        element.click();
        #driver.find_element(By.XPATH, "//*[@id='resume-display-buttonHeader']/div[2]/span[1]").click()
        #time.sleep(1)
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        #time.sleep(1)
    except:
        print("Error on resume")
        return -1

## @brief Function that handles past job experience submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def pastJob(driver):
    
    try:
        #time.sleep(0.5)
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        #time.sleep(1)
    except:
        print("Error on upload past job exp")
        return -1

## @brief Function that handles user cover letter submission
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def coverLetter(driver):
    
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button")))
        element.click();
        #time.sleep(1)
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        #time.sleep(1)
    except:
        print("Error on cover letter upload")
        return -1
## @brief Function that handles user final user info submission and application
#  @param driver: Webdriver for chrome which parses and interacts with the HTML from a given website
def reviewApp(driver):
    try:
        #driver.find_element(By.XPATH, "//*[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button").click()
        print("Not submitting final submission")
        return
    except:
        return ValueError("Error on final submission")


if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    #url = "https://ca.indeed.com/viewjob?jk=69fcb3526cf27694&q=engineer&l=collingwood&tk=1fvs137cqsa5r802&from=web&advn=5498045691600945&adid=375760518&ad=-6NYlbfkN0B8-duVi6k7gERyiVpl1MQjI7lORbHkp4egcwb7uU1fZRq-pfsnquTR1sdLjbE2a9lTrd0RR3bGYBtsbX16K-gxgnANGADnWA2dRJZp0DLKgFM3DAmeaHzELKRVrBbXaRHc-Zk64WTtZU_wvJ9-l0TYgyxvIUExRGOa4oZu648GNPdWNV8gQg5TveApwRkbLKZXNjB5O6moWiliiZWQVl0U9EgMjB3W6EZY08ITMKn470hc-ESh-4apoOoNvh5TLvW5O5bk4oNfbX7_3NjZ3ySaXxJ08zzVeb2QVqUXooHxxN9lhAYeRjwIs4gDIar5u3XurrqIcP3K3RdbEOTCNW3rao3JjtyYgzMK1HeAhlnZ0zWmOl80DqK8uDnPIewAl54%3D&pub=4a1b367933fd867b19b072952f68dceb&vjs=3"
    url = "https://ca.indeed.com/viewjob?cmp=C.-F.-Crozier-%26-Associates&t=Engineering%20Intern&jk=62be08b1e0a77348&q=engineer&vjs=3"
    driver.get(url)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='indeedApplyButton']/div").click()
    while driver.current_url != "https://m5.apply.indeed.com/beta/indeedapply/form/contact-info":
        continue

    runApplication(driver)
    #driver.get(url)

