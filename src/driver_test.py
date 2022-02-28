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

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://ca.indeed.com/')

page_source = driver.page_source
soup = BeautifulSoup(page_source)

print(soup.prettify())
