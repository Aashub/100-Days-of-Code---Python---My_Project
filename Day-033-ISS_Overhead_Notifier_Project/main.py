import requests
from datetime import datetime
from smtplib import  SMTP
import time

MY_LAT =  # Your latitude
MY_LONG =  # Your longitude

def send_mail():
    """this function will create the secure connection between sender and receiver using smtp module. and send the message"""

    my_email = "anonyasteroid@gmail.com"
    password = "jiwvmkgqvdmooxdu"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="anonyasteroid@gmail.com",
                            msg=f"Subject: Remainder! \n\nISS satellite is just above you look at it.")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunset_response.raise_for_status()
data = sunset_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = data["results"]["sunset"].split("T")[1].split(":")
sunset.pop(2)


sunset = [int(time) for time in sunset]

# this changes we are doing because as per UTC time at 12:35 sunset happened so in order to make it as per indian standard time we need to add 5: 30 in UTC time of 12: 35 pm to get the correct time of sunset
for modify_time in sunset:
    if modify_time == 35:
        sunset[0] = 13 + 5   # 1 represents after adding 35 it will became 13 pm & 5 represents adding extra 5 hours to get actual sunset time
        sunset[1] = 5   # 5 represents 5 minute after adding 35 minutes extra in 12:30 UTC time


hour = datetime.now().hour
minute = datetime.now().minute

time_now = (hour, minute)
sunset_time = (sunset[0], sunset[1])

# when iss latitude and longitude are in range of my latitude and longitude then condition become true and sunset time and current time also matches than sen_mail will get called.
while True:
    time.sleep(60)
    if (iss_latitude <= MY_LAT + 5 or iss_latitude >= MY_LAT - 5) and (iss_longitude <= MY_LONG + 5 or iss_longitude  >= MY_LONG - 5):

        if time_now == sunset_time:
            send_mail()




