import requests
from datetime import datetime, timedelta
import os

CITY_SEARCH_ENDPOINT = os.environ.get("AMADEUS_CITY_SEARCH_ENDPOINT")
FLIGHT_OFFER_SEARCH_ENDPOINT  = os.environ.get("AMADEUS_FLIGHT_OFFER_SEARCH_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, city_list, AMADEUS_TOKEN):
        self.AMADEUS_TOKEN = AMADEUS_TOKEN
        self.city_list = city_list
        self.data_list = []
        self.iata_list = []

        header = {
            "Authorization": f"Bearer {self.AMADEUS_TOKEN}"
        }

        for city in range(len(self.city_list)):

            parameters = {
                "keyword": city_list[city],
                "max": 3
            }

            # by using amabeus api this request will fetch data of iata city code.
            self.response = requests.get(url=CITY_SEARCH_ENDPOINT, params= parameters, headers= header)
            self.data_list.append(self.response.json()["data"])

        self.get_iata_data()

    def get_iata_data(self):
        """this method will update the iata_list with city code."""
        self.iata_list = [code[0]["iataCode"] for code in self.data_list]

    def finding_flights(self):
        """this method will fetch the raw data from the amabeus api as per the below required parameter and return flight data dictionary and maximum result of each iata code."""

        for_days = 7
        for_date_iteration = 1
        max_result_each_code = 5
        today = datetime.now()
        flight_data_list = []

        header = {
            "Authorization": f"Bearer {self.AMADEUS_TOKEN}"
        }

        for days in range(for_days):
            dates = today + timedelta(days=for_date_iteration)
            flight_date = dates.strftime("%Y-%m-%d")

            for code in self.iata_list:
                parameters = {
                    "originLocationCode": "DEL",
                    "destinationLocationCode": code,
                    "adults": 1,
                    "max": max_result_each_code,
                    "departureDate": flight_date
                }

                # this request will fetch the flight data and store them in a list flight_data_list
                output_response = requests.get(url=FLIGHT_OFFER_SEARCH_ENDPOINT, params=parameters, headers=header)
                flight_data_list.append(output_response.json())

            for_date_iteration += 1

        return flight_data_list, max_result_each_code


