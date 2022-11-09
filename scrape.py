from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Scraper():
    def __init__(self, url):
        self.url = url

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-dev-shm-usage')

        self.driver = webdriver.Chrome('chromedriver', options = chrome_options)
        self.driver.get(url)
        page = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "sparkDistanceTxt")))


    def findDistance(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        distance = soup.find('span', class_="closest-strike-distance")

        return distance.text


    def closeScraper(self):
        self.driver.close()
