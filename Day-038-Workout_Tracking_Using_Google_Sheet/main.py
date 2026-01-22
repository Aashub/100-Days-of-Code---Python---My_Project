import requests
from datetime import datetime
import os

# Fetching required values from environment variables
APP_ID = os.environ["NUTRITION_APP_ID"]
API_KEY = os.environ.get("NUTRITION_API_KEY")
USER_NAME = os.environ.get("SHEETY_USER_NAME")
BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEETY_SHEET_ENDPOINT")

exercise_endpoint = f"https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

# This dictionary stores the user input describing the exercises performed Nutritionix API converts this natural language text into structured exercise data
request_body = {
       "query": input(f"Tell me which exercises you did :").title(),
}

# authentication
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Sending POST request to Nutritionix API with exercise details, The API responds with parsed exercise information
response = requests.post(url= exercise_endpoint, json=request_body, headers= headers)
result = response.json()["exercises"][0]


#*************************sheety api**********************************

date_time = datetime.now()

# data that will go in teh google sheet
new_data = {
    "workout":{
        "date": date_time.strftime("%d/%m/%Y"),
        "time": date_time.strftime("%X"),
        "exercise": result["name"],
        "duration": result["duration_min"],
        "calories": result["nf_calories"]
}
}

# authentification
HEADER = {
    "Authorization": BEARER_TOKEN
}

# this post request will add all the new data which we have fetched in the google sheet.
response = requests.post(url= SHEET_ENDPOINT, json= new_data, headers= HEADER)
print(response.text)





