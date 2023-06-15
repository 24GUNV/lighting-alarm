# Lightning Alarm Tool
This program is run on a microcontroller to periodically scrape data off [WeatherBug](https://www.weatherbug.com/) to see how close lightning is to our school. A wiring signal is sent to turn on the lightning alert system if the distance drops below a certain threshold.

## Table of Contents
* [General Info](#general-information)
* [Dependencies](#dependencies)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information
- The program periodically scrapes data off [WeatherBug](https://www.weatherbug.com/) using Selenium and Beautiful Soup in order to see how close lightning is to our school. If the nearest lightning strike is within a certain proximity, a signal is sent out from the microcontroller to turn on/off the lightning alarm lights.
- The program automates the lightning alarm lights at the school. Instead of having a teacher operating the lights, the program automates the process.


## Dependencies
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
``pip install -r requirements.txt``

Make sure that port 5 or port 6 of the microcontroller is connected to the lights

## Usage
`python lights.py`
Note: This program is intended to be ran on a microcontroller. An error will occur otherwise.


## Project Status
Project is: _in progress_


## Room for Improvement
To do:
- Add more safety checks in the program
- Final touches


## Contact
Created by [@24GUNV](https://github.com/24GUNV) - feel free to contact me!

Created by [@Chakr3y](https://github.com/Chakr3y)
