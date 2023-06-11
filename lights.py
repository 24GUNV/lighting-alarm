import wiringpi
import time, logging
from scrape import Scraper
import re

# Constants
DANGERDISTANCE = 5 #km

# GPIO setup
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(5, 1)

# Scraper setup
scraper = Scraper("https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.66744&lon=100.64206&v=1.2.0")

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
        if re.match(r'^-?\d+(?:\.\d+)$', distance) is None: # Checks for if it isnt a float
            continue

        logging.info(f"Distance: {distance}")

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

        time.sleep(300)


except KeyboardInterrupt:
    logging.info("User ended program")

except Exception as error:
    logging.fatal("Error detected")
    print(error)

finally:
	wiringpi.digitalWrite(5, 0)
	wiringpi.digitalWrite(6, 0)
	scraper.closeScraper()
	logging.info("Ending program")