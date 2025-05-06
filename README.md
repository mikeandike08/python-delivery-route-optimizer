# python-delivery-route-optimizer
Uses multiple addresses to get the shortest route between them with a google maps api as a web app

## Description

Used a google maps api in order to take in multiple addresses to then return the shortest route between them, little animated car to simulate driving.

## HOW TO USE

- Make sure to have to have the necessary requirements, check below for more info
- If you want a quick and easy experience, import a csv of your addresses and you can get going
- Don't worry! If not, you can simply type your addresses in the box, only use commas to separate addresses
- VERY IMPORTANT make sure to include the city name in the address ex: 123 john doe city, NO commas
- Once you submit and everything is okay you can calculate the route, either by default(will not loop back) or use the checkbox for looping(utilizes TSP)


## Disclaimer

- I went a little too try-hard for my high school python project, but I wanted to learn, so this is my first time using API's and you can tell from my past projects I've never used them, so I did unfortunately have to use a bit of ai in order to figure this stuff out, but I did learn a lot, specifically about Flask and how to pass variables through there so I'm happy about that
- If you're trying to run this through an IDE and the website isn't loading, make sure to try running it through console.

## HOW TO RUN

- Install the entire repository.
- If you decide to open the project through an IDE
  - Run it and a terminal should pop up, if you have issues try the second way.
- Open your terminal and navigate to the project, run -- py app.py
- Copy the IP address the terminal gives you and paste it into a browser of your choosing.

## Python Requirements

- Flask (3.1)
- Jinja 2
- requests

## How to get Google Maps API Key (Free)

- Go to the Google Cloud Console : https://console.cloud.google.com/
- Create a New Project
	- Click the project dropdown at the top
	- Click "New Project"
	- Name your project and click "Create"
- Enable Maps APIs
	- With your project selected, go to :  https://console.cloud.google.com/marketplace
	- Search for and enable the following APIs:
		- Maps JavaScript API
		- Directions API
		- Geocoding API
- Create Credentials
	- Go to APIs & Services > Credentials.
	- Click "create Credentials" -> "API Key".
	- Copy the Key
- Now Copy that key and replace the "PUT API KEY HERE" with your api key, one in routeCalc.py and map.html
