#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# ************the below object will fetch all the city_list, iata_list if they are present***********
fetch_data = DataManager()
flight_search_city = fetch_data.city_list
iata_code_list = fetch_data.iata_list
lowest_price_list = fetch_data.sheet_price


def populate_iata_code():
    """this function will populate the iata code in the sheet and return iata code list for further process"""

    flight_data = FlightData(iata_code_list)
    new_token = flight_data.response_output["access_token"]
    amabeus_token = new_token

    # the flight_search object will help in find the iata_code to populate in google sheet by calling amabeus api,
    flight_search = FlightSearch(flight_search_city, amabeus_token)

    # this method will fill the IATA_CODE in the Google sheet
    IATA_CODE = flight_search.iata_list
    # fetch_data.populate_iata_code(IATA_CODE)

    return IATA_CODE


# if even first code is empty than the below function get called to populate the sheet with iata code
if len(iata_code_list[0]) == 0:
    iata_code_list = populate_iata_code()

# ************ flight_data.response_output will be responsible to give us the amabeus token without this we can't get raw flight data *************
flight_data = FlightData(iata_code_list)
new_token = flight_data.response_output["access_token"]
amabeus_token = new_token

# **************also flight_search object will call finding_flight method to fetch raw data from amabeus api****************
flight_search = FlightSearch(flight_search_city, amabeus_token)
raw_flight_data, max_result = flight_search.finding_flights()

# ************ flight_data object will call the find_cheapest_flight() method to fetch the cheapest flight data ***************
cheapest_flight_data = flight_data.find_cheapest_flight(raw_flight_data, lowest_price_list, max_result)

# *********** notification_manager object call the send_notification method to send the notification on telegram *****************
notification_manager = NotificationManager()
notification_manager.send_notification(cheapest_flight_data)

    



