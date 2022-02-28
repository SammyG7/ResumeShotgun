import sys
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driverLocation = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=driverLocation)

#keyword and location from user input module
keyword = ""
location = ""

def search(keyword, location):
    driver.get("https://ca.indeed.com/")
    driver.find_element_by_id("text-input-what").send_keys(str(keyword))
    time.sleep(.5)

    driver.find_element_by_id("text-input-where").send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id("text-input-where").send_keys(Keys.DELETE)
    driver.find_element_by_id("text-input-where").send_keys(str(location))
    time.sleep(0.5)
    driver.find_element_by_class_name("yosegi-InlineWhatWhere-primaryButton").click()
    print(driver.current_url)

if __name__ == "__main__":
    search(sys.argv[1],sys.argv[2])
