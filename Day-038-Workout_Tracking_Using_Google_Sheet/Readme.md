# Day 38 – Workout Tracking Using_Google Sheet

## Project Overview

This project is a Workout Tracker application built using Python. The app allows the user to enter exercises performed in natural language, than relevant details of workout data from the `Nutritionix Exercise API` is fetched , and then logs the workout details (date, time, exercise name, duration, and calories burned) into a Google Sheet using the `Sheety API`. The project focuses on API integration, environment variables, handling JSON responses, and secure authentication using bearer tokens also while building this project i learned about how to add environment variable in the pycharm.

## What I Have Learned

* **Working with APIs**: Revised about how to send POST requests, pass headers and JSON payloads, and handle API responses using the requests library.

* **Nested Dictionaries & JSON Handling**: Improved understanding of extracting required values from nested JSON responses returned by APIs.

* **Environment Variables**: Learned how to securely store and access sensitive information such as API keys, app IDs, and bearer tokens using environment variables instead of hard-coding them.

## How It Works

* **User Input**: The program asks the user to enter the exercises they performed in natural language (for example: walking, running, weight training). 

* **Nutritionix API Request**: The user input is sent to the Nutritionix Natural Exercise API and then The API processes the text and returns structured workout data such as exercise name, duration(in minute), calories burned.

* **Date & Time Handling**: The current date and time are captured using the datetime module. also The values of date time are formated using the `strftime() method to match the Google Sheet structure.

* **Sheety API Integration**: The workout data is structured according to Sheety’s expected format in a `new_dataa` dictionary. and than a POST request is sent to the Sheety API using a bearer token for secure authentication. after that the data is automatically added as a new row in the connected Google Sheet.

## Project Highlights

* Integrated two different APIs in a single project
* Practiced secure handling of API keys and tokens
* Learned how to log real-world data into Google Sheets programmatically
* Learned how to securely store and access sensitive information such as API keys, app IDs, and bearer tokens using environment variables instead of hard-coding them 