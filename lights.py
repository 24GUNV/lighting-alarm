import wiringpi
import time, logging
from scrape import Scraper
import re

# Constants
DANGERDISTANCE = 50 #km

# GPIO setup
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(5, 1)

# Scraper setup
scraper = Scraper("https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.75398&v=1.2.0")

# Logger setup
logging.basicConfig(filename='log.txt',
					filemode='a',
					format='%(asctime)s %(name)s %(levelname)s- %(message)s',
					datefmt='%H:%M:%S',
					level=logging.NOTSET)
logging.disable(logging.DEBUG)
logging.getLogger("selenium.webdriver.common.selenium_manager").disabled = True
logging = logging.getLogger("Lightning-Alarm")


try:
	inArea = False
	while (True):
		distance = scraper.findDistance()

		if re.match(r'^-?\d+(?:\.\d+)$', distance) is None: # Checks whether distance isnt a float
			continue

		# Checks if distance is in danger area
		if (float(distance) < DANGERDISTANCE):
			if (not inArea):
				logging.info("Lightning entered area")
				inArea = True

			# Outputs to the wires
			wiringpi.digitalWrite(5, 1)
			wiringpi.digitalWrite(6, 1)
		else:
			if (inArea):
				inArea = False
				logging.info("Lightning left area")

			wiringpi.digitalWrite(5, 0)
			wiringpi.digitalWrite(6, 0)


		logging.info(f"Distance: {distance} ")

		time.sleep(300) # Next cycle in 5 minutes

except KeyboardInterrupt:
	logging.info("User ended program")

except:
	logging.fatal("Error detected")

finally:
	wiringpi.digitalWrite(5, 0)
	wiringpi.digitalWrite(6, 0)
	scraper.closeScraper()
	logging.info("Ending program")