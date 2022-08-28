from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = "https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.75398&lon=100.50144&v=1.2.0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
    
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get(url)
page = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "sparkDistanceTxt")))

iterations = 10
for i in range(10):
	soup = BeautifulSoup(driver.page_source, "html.parser")


	distance=soup.find_all('span', class_="closest-strike-distance")
	print(distance)
	
	time.sleep(5)

driver.close()