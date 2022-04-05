## @file userProfile.py
#  @details Depreciated?
#  @author Gavin Jameson
#  @brief user profile module
#  @date Apr 5, 2022

import requests
import selenium.webdriver
import os.path
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

## @brief Checks version of Chrome
#  @return String indicating version of Chrome
def checkChromeVersion():
    platform = sys.platform
    ser = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service = ser)
    driver.get("https://www.google.com")
    if "browserVersion" in driver.capabilities:
        return driver.capabilities["browserVersion"]
    else:
        return driver.capabilities["version"]

## @brief Checks if driver version is downloaded
#  @param version String indicating version to check for
#  @return Boolean True if chromedriver has been downloaded, False if not
def hasDriver(version):
    path = os.path.join("ChromeDrivers", stem(version), "chromedriver.exe")
    return os.path.isfile(path)

## @brief Attempts to download a driver for a given version of Chrome
#  @param version String indicating version of CHROME BROWSER to
#  attempt to download a driver for
#  @return Boolean for success of download
def getDriver(version):
    path = os.path.join("ChromeDrivers", stem(version), "chromedriver.exe")
    driverVersionUrl = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{stem(version)}"
    response = requests.get(driverVersionUrl)
    driverVersion = response.text
    print(driverVersion)
    #file = open(path)
    #file.write(response.content)

## @brief Shortens version number to remove last part
#  @param version String to shorten
#  @return String identical to input with last period and everything
#  after it removed
def stem(version):
    return ".".join(version.split(".")[:-1])

if __name__ == "__main__":
    cv = checkChromeVersion()
    print(f"Your Chrome version is: {cv}")
    d = "Yes" if hasDriver(cv) else "No"
    print(f"Do you have the driver for it: {d}")
