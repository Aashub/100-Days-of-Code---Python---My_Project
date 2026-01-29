import requests
import os


LOGIN_ID = os.environ.get("AMADUES_LOGIN_ID")
API_KEY = os.environ.get("AMADEUS_API_KEY")
API_SECRET = os.environ.get("AMADEUS_API_SECRET")
TOKEN_CREATE_ENDPOINT = os.environ.get("AMADEUS_ENDPOINT")


class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, iata_list):

        self.AMADEUS_TOKEN = ""
        self.iata_list = iata_list

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        # this request will fetch token id without token id without token id we can get flight data
        self.response = requests.post(url=TOKEN_CREATE_ENDPOINT, data=body, headers=header)
        self.response_output = self.response.json()

    def find_cheapest_flight(self, flight_data, sheet_lowest_price_list, max_result):
        """this method will create a dict of cheapest flight data from raw data and return cheapest flight data in the form of dict."""


        # this list comprehension is used for getting destination code from flight data from links
        destination_code = [str(iterate["meta"]["links"]["self"]) for iterate in flight_data]

        # this `nested dict comprehension` is used to create dictionary so that all the required cheapest flight data can be stored, each iata code has its own dictionary.
        flight_lowest_price_dict = {code: {"prices": [], "city_name": None, "last_ticketing_date": None, "destination_location_code": None,
                                           "origin_location_code": None} for code in self.iata_list}


        # this for loop stores all prices of each iata code in their specific dictionary key in flight_lowest_price_dict
        for code in flight_lowest_price_dict:
            iterate = 0
            for dest_code in destination_code:

                # if flight_lowest_price_dict key match with destination_code list index value than for that iata code all prices will be added in "prices key"  which is empty list with their parent key of IATA code
                if code in dest_code:
                    for num in range(max_result):

                        try: # iterate variable help in jump from one list index to another list index
                            flight_lowest_price_dict[code]["prices"].append(float(flight_data[iterate]["data"][num]["price"].get("grandTotal")))
                        except:
                            pass
                iterate += 1

        iterate = 0
        key_to_remove_list = []
        # this for loop will help in find which flight_lowest_price_dict key prices are greater than sheet prices for that particular iata code so we can remove that key.
        for flight_lowest_price in flight_lowest_price_dict:
            for sheet_lowest_price in sheet_lowest_price_list:

                try: # iterate variable help from changing sheet list iata_code
                    if min(flight_lowest_price_dict[flight_lowest_price]["prices"]) <= sheet_lowest_price_list[iterate]:
                        break
                    else:
                        key_to_remove_list.append(flight_lowest_price)
                        break
                except ValueError:
                    pass
            iterate += 1

        # this for loop will delete those key from flight_lowest_price_dict which has greater prices from sheet prices for that particular iata code
        for remove_Key in key_to_remove_list:
            del flight_lowest_price_dict[remove_Key]

        # this nested for loop will help in add last ticketing date, destination iata code and origin location iata code in a  `flight_lowest_price_dict dictionary`
        for code in flight_lowest_price_dict:
            for iterate in flight_data:
                for num in range(max_result):
                    try:
                        if min(flight_lowest_price_dict[code]["prices"]) == float(iterate["data"][num]["price"]["grandTotal"]):

                            index_to_fetch_data = flight_data.index(iterate)

                            flight_lowest_price_dict[code]["last_ticketing_date"] = flight_data[index_to_fetch_data]["data"][0]["lastTicketingDate"]

                            # the below variable help in prevent destination_location_code to be stored as None because in some cases `SEGMENTS` size could be 1 or 2.
                            index_for_destination = len(flight_data[index_to_fetch_data]["data"][0]["itineraries"][0]["segments"])

                            flight_lowest_price_dict[code]["destination_location_code"] = flight_data[index_to_fetch_data]["data"][0]["itineraries"][0]["segments"][index_for_destination - 1]["arrival"]["iataCode"]

                            flight_lowest_price_dict[code]["origin_location_code"] = "DEL"

                    except ValueError:
                        pass

                    except IndexError:
                        pass

        return flight_lowest_price_dict