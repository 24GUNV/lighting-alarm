import wiringpi
import time, logging
from scrape import Scraper
from datetime import datetime

# Constants
DANGERDISTANCE = 50 #in km

# GPIO setup
wiringpi.wiringPiSetupGpio()
scraper = Scraper("https://lxapp.weatherbug.net/v2/lxapp_impl.html?lat=13.75398&v=1.2.0")
wiringpi.pinMode(5, 1)

# Logging setup
logging.basicConfig(filename="log.txt", level=logging.INFO)
log = logging.getLogger("lights")


try:
    inArea = False
    while (True):
        distance = scraper.findDistance()
        if (distance.isnumeric() and int(distance) < DANGERDISTANCE):
            if (not inArea):
                log.info("LIGHTNING IN THE AREA")
                inArea = True

            wiringpi.digitalWrite(5, 1)
            wiringpi.digitalWrite(6, 1)
        else:
            if (inArea):
                inArea = False
                log.info("LIGHTNING LEFT THE AREA")

            wiringpi.digitalWrite(5, 0)
            wiringpi.digitalWrite(6, 0)


        currentTime = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        log.info(f"Distance of lighting as of  {currentTime}: {distance} ")

        time.sleep(5)

except KeyboardInterrupt:
    wiringpi.digitalWrite(5, 0)
    wiringpi.digitalWrite(6, 0)
    scraper.closeScraper

    print("Ending program")
