from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Web address for data scraping
url = "https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.66744&lon=100.64206&v=1.2.0"


class Scraper():
	def __init__(self, url):
		self.url = url

		# Setting webdriver configs
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('disable-dev-shm-usage')
		chrome_options.add_argument('--disable-gpu')

		# Loading url into webdriver
		self.driver = webdriver.Chrome('chromedriver', options = chrome_options)
		self.driver.get(url)
		page = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "sparkDistanceTxt")))

	def findDistance(self):
		# Checks whether the webpage is still updating
		originalPage = BeautifulSoup(self.driver.page_source, "html.parser")
		distance=originalPage.find_all('span', class_="closest-strike-distance")[0].text
		
		time.sleep(1)
 
		newPage = BeautifulSoup(self.driver.page_source, "html.parser")
		newDistance = newPage.find_all('span', class_="closest-strike-distance")[0].text

		# Refreshes the page until the number is constant
		while newDistance != distance:
			originalPage = newPage
			distance=newDistance

			time.sleep(1)
			newPage = BeautifulSoup(self.driver.page_source, "html.parser")
			newDistance = newPage.find_all('span', class_="closest-strike-distance")[0].text
		
		else:
			distance = newDistance

		return distance


	def closeScraper(self):
		self.driver.close()
