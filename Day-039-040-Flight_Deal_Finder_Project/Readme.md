# Day 39-40 – Flight Deal Finder

## Project Overview

This project is a Flight Deal Finder and Price Alert application built using Python. The app fetches destination cities and their lowest expected prices from a Google Sheet using Sheety API, and searches for real flight prices using the Amadeus Flight APIs, compares them with sheet prices, and sends Telegram notifications when a cheapest flight deal is found only for those cities which has cheapest price as compared to sheet price for that particular same city=. The project mainly focuses on working with multiple APIs, handling complex JSON responses, environment variables, and sending real-time notifications using Telegram. while building this project i have used all the things which i learned so far and also learned few more things while building this project. 

## What I Have Learned

* **Working with Nested JSON Data**: Improved skills in extracting required values like prices, IATA codes, dates, and locations from deeply nested JSON responses.

* **Environment Variables**: Practiced securely storing API keys, secrets, tokens, and endpoints using environment variables instead of hard-coding them.

* **API Integration**: Revised how to work with multiple APIs together such as Amadeus APIs, Sheety API, and Telegram Bot API.

* **Authentication & Tokens**: Learned how to generate OAuth2 token-based authentication token and how to use these access tokens securely.

* **Nested Dictionary Comprehension**: Learned how to create nested dictionary using nested dictionary comprehension how to store data into them.

* **del statement**: Learned how to use del statement to delete dictionary key in python.

## How It Works

* **`DataManager class`**: The DataManager class fetches city names, IATA codes, and lowest expected prices from a Google Sheet using the Sheety API. If IATA codes are missing in the sheet, the program automatically calls populate_iata_code() function this function than calls `Flight_data() class by using this class we create access token which is required to call Flight_search() class after getting access token in Flight_search() class access token and city list passes which will create IATA CODE list and by using flight search object we store them in a IATA CODE variable and return that variable so program can use them.

* **`FlightData class`**: If everything goes fine and no need to generate IATA code list The `FlightData class` generates an OAuth2 access token using Amadeus API credentials. This token is required to make authorized requests to `FlightSearch()` class for fetching data of IATA CODE using Amadeus api and also fetching raw flight offers data from amadeus flight offer search api.

* **`FlightSearch class`**: FlightSearch class required two parameters access token and city list data by passing this two parameters and by using flight_search object it calls finding_flights() method which will give us the raw data of flight offers by calling amadeus flight search api and also return max_result for each IATA code for further data filtering.  

* **`find_cheapest_flight()`**: By using flight_data object than we call `find_cheapest_flight()` method which will do further data filtering and give us clean data dictionary which will have only cheapest flight data only, this method take three arguments raw_flight_data, lowest_price_list, max_result by using this three arguments this method filter out raw data and give us dictionary data of those IATA code only which has lesser price than sheet price for that IATA code only like list of prices, destination IATA code, Origin IATA code, last ticketing date in the form of dictionary.

* **`NotificationManager()`**: After getting returned data from `find_cheapest_flight()` method it get stored in cheapest_flight_data variable and this variable than passed in send_notification() method which will later than call Telegram Bot API and send notification of flight offers.

* **`main.py`**: this file will be responsible for creating object of all classes and calling their methods.

## Limitations

* I am unable to automate the process to send the message on daily basis because in order to do that i had to buy a subscription of platform like pypthonanywhere which helps us to automate this process to send this kind of notification on daily basis.

## Project Highlights

* This is a capstone project but still i have build this whole project by myself without looking into any hint.
* Used three different API to build this Project 
* Practiced secure handling of API keys and tokens
* Learned how to fetch, update and access real-world data from the  Google Sheets programmatically
* Practiced secure handling of API keys, API token, and credential using environment variables
* learned about nested dictionary comprehension and how to use them and store data into them
* learned about del statement to delete specific key in a dictionary.
