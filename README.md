# Lightning Alarm Tool
This program periodically scrapes data off [WeatherBug](https://www.weatherbug.com/) to see how close lightning is to our school. A microcontroller then sends signals out accordingly

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information
- The program periodically scrapes data off [WeatherBug](https://www.weatherbug.com/) using a combination of Selenium and Beautiful Soup in order to see how close lightning is a to our school. Based on the data, a signal could be sent out from the microcontroller to turn on and off the lightning alarm lights
- The program intends to automate activating the lightning alarm lights at the school. Instead of having a teacher manually monitor the distance to the lightning and having to go turn the lights on, the program intends to do it automatically


## Technologies Used
- WiringPi - version 2.60.1
- Selenium - version 4.9.1
- beautifulsoup4 - version 4.11.1


## Features
- Scraping data of distance to closest lightning
- Automatic activation of lights
- Deployment on a microcontroller


## Screenshots
Example of the output of the scraped data
![outputexample](https://user-images.githubusercontent.com/38719890/187079004-465fd9b8-9b43-4d75-96dd-a73b26bd33ac.PNG)

Map from Weatherbug
![weathermap](https://user-images.githubusercontent.com/38719890/187079007-ba0daa2e-decf-4625-848d-3e0c5ac22292.PNG)


## Setup
Install the required libraries
``pip install wiringpi``
``pip install selenium``
``pip install beautifulsoup4``

Make sure that port 5 or port 6 of the microcontroller is connected to the lights

## Usage
`python lights.py`


## Project Status
Project is: _in progress_


## Room for Improvement
Room for improvement:
- More efficient way to check whether website is refreshing

To do:
- Add more safety checks in the program
- Make it easier to config


## Contact
Created by [@24GUNV](https://github.com/24GUNV) - feel free to contact me!

Created by [@Chakr3y](https://github.com/Chakr3y)
