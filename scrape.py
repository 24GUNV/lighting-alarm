from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, logging

# Web address for data scraping
url = "https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.66744&lon=100.64206&v=1.2.0"

# Logger setup
logging.basicConfig(filename='log.txt',
		    		filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s- %(message)s',
		     		encoding='utf-8',
				    datefmt='%H:%M:%S',
					level=logging.NOTSET)
logging.disable(logging.DEBUG)
logging.getLogger("selenium.webdriver.common.selenium_manager").disabled = True
logging = logging.getLogger("Lightning-Alarm")


# Configuring webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setting up url to be scraped
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get(url)
page = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "sparkDistanceTxt")))

logging.info("Starting logging session")

try:
	while True:
		# Checks whether the webpage is still updating
		originalPage = BeautifulSoup(driver.page_source, "html.parser")
		distance=originalPage.find_all('span', class_="closest-strike-distance")[0].text

		time.sleep(1)

		newPage = BeautifulSoup(driver.page_source, "html.parser")
		newDistance = newPage.find_all('span', class_="closest-strike-distance")[0].text

		while newDistance != distance:
			originalPage = newPage
			distance=newDistance

			time.sleep(1)
			newPage = BeautifulSoup(driver.page_source, "html.parser")
			newDistance = newPage.find_all('span', class_="closest-strike-distance")[0].text
		else:
			distance = newDistance

		# Logs the distance into the log
		logging.info(f"Distance: {distance}")
		
		time.sleep(300) # Waits for 5 mins until the next cycle
		
except KeyboardInterrupt:
	logging.info("User ended program")
except:
	logging.fatal("An Error has occured")
finally:
	logging.info("Program ended")
	driver.close()