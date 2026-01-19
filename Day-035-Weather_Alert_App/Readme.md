# Day 35 – Weather Alert Email Notification App

## Project Overview

This project is a Weather Alert Email Notification application built using Python. The app uses the OpenWeatherMap (OWM) Forecast API to check upcoming weather conditions for a specific location based on latitude and longitude. If rain is expected in the near future, the program automatically sends an email notification to the user reminding them to carry an umbrella. This project focuses on working with APIs, environment variables, list comprehension, and sending emails securely using SMTP.

## What I Have Learned

* **Nested_Dict_%_list**: Revised how to work with JSON data and extract required information from nested dictionaries and lists.

* **list comprehension**: Revised about the list comprehensions to simplify looping and data extraction logic.

* **Environment variables**: Learned the importance of using environment variables to store sensitive data like API keys and email passwords securely using environment variables.

How It Works

* **Weather API Request**: The program sends a request to the OpenWeatherMap 5-day / 3-hour forecast API using latitude, longitude, API key, and count parameters. The response is received in JSON format and stored for further processing.

* **Weather Condition Analysis**: Using list comprehension, the program extracts weather condition codes and descriptions(weather status) from the API response. If any weather condition code is less than 700, it indicates rain or similar weather conditions.

* **Rain Detection Logic**: The program checks each weather condition code. If rain is detected, a boolean flag `will_rain` is set to True, and the corresponding weather description(weather status) is stored in a variable `weather_type`.

* **Email Notification**: If rain is expected, the `send_mail(weather_type)` is triggered. This function establishes a secure SMTP connection with Gmail, logs in using the sender’s email credentials, and sends an email notification to the user with the weather description and a reminder to bring an umbrella.

## Project Highlights

* Practiced API integration and JSON data handling.

* learned about API keys and environment variable and how to use them.
