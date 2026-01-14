# Day 32 - ISS Overhead Notifier Project 

## Project Overview

This project is an ISS (International Space Station) Overhead Notifier that automatically checks the current position of the ISS and sends an email alert when the ISS is passing near the user’s location at sunset time. The application uses real-time data from public APIs to fetch the ISS’s current latitude and longitude and compares it with the user’s geographical coordinates. It also retrieves sunrise and sunset times in UTC and converts them to Indian Standard Time (IST). If the ISS is within ±5 degrees of the user’s location and the current time matches the local sunset time, an email notification is sent using SMTP. Through this project, I learned how to work with APIs.

---

## What I Have Learned

* How to use the requests library to fetch live data from APIs.
* How to handle API responses using json() and error handling with raise_for_status().

## How It Works 

* **Requests Module for ISS position**: The program first calls the Open Notify API to get the current latitude and longitude of the ISS using `http://api.open-notify.org/iss-now.json` link, The received values are converted into floating-point numbers for comparison. 

* **Requests Module for sunset time**: Then  program calls the Sunrise-Sunset API using the user’s latitude and longitude by using `https://api.sunrise-sunset.org/json` this API returns time in UTC format so later  The sunset time is extracted and converted into indian standard time(IST) by adding 5 hours and 30 minutes.

* **Location Check**: The ISS is considered “overhead” if, ISS latitude and longitude is within ±5 degrees of the user’s latitude and longitude location than it matches the current time with the sunset time and if it does matches than `send_mail()` function get called.

* **`send_mail()`**: The send_mail() function creates a secure SMTP connection with Gmail’s server. After logging in, it sends the personalized remainder message to the user email address that the ISS is passing look into the sky, Once the email is sent, the connection is closed automatically using the with statement.

## How It Works 
learned how to use public API using requests library 