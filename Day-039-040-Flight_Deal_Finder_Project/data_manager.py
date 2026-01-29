import requests
import os

USERNAME = os.environ.get("SHEETY_USERNAME")
SHEET_ENDPOINT = os.environ.get("SHEETY_SHEET_ENDPOINT")
SHEET_UPDATE_ENDPOINT = os.environ.get("SHEETY_UPDATE_ENDPOINT")
AUTHORIZATION_TOKEN = os.environ.get("SHEETY_AUTHORIZATION_TOKEN")

HEADER = {
            "Authorization": AUTHORIZATION_TOKEN
        }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.city_list = []

        self.sheety_api_endpoint = SHEET_ENDPOINT

        # this get request from sheety  api  will give us raw data from the google sheet
        self.response = requests.get(url= self.sheety_api_endpoint)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()["prices"]

        # list comprehension to get city_list, iata_list, and sheet_price_list
        self.city_list = [get_cities["city"] for get_cities in self.sheet_data]
        self.iata_list = [code["iataCode"] for code in self.sheet_data]
        self.sheet_price = [price["lowestPrice"] for price in self.sheet_data]

    def populate_iata_code(self, iata_code):
        """This method will update the IATA code in google sheet if those code are not present in a sheet."""

        num = 2
        for code in iata_code:

            new_data = {
                "price": {
                    "iataCode": code
                }
            }

            # this put request update each IATA code in a sheet
            self.response = requests.put(url=f"{SHEET_UPDATE_ENDPOINT}/{num}", json=new_data, headers=HEADER)
            num += 1



