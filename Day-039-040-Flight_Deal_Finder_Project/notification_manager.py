import requests
import os


BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_notification(self, cheap_flight_dict):

        for code in cheap_flight_dict:
            if cheap_flight_dict[code]["prices"] == []:
                pass
            else:

                parameters = {
                    "chat_id": CHAT_ID,
                    "text": f"✈️ Low price Alert! Only €{min(cheap_flight_dict[code]["prices"])}\nfly from {cheap_flight_dict[code]["origin_location_code"]}"
                                f" to {cheap_flight_dict[code]["destination_location_code"]} do ticketing before {cheap_flight_dict[code]["last_ticketing_date"]}"
                    }

                telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

                response = requests.get(url=telegram_url, params=parameters)
                response.raise_for_status()
                response.json()




