import requests
from smtplib import SMTP

def send_mail(weather) :
    """this function will create the secure connection between sender and receiver using smtp module and take input of weather condition and send the mail."""

    my_email = "@gmail.com"
    password = ""

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Weather Remainder! \n\nTheir likely going to happen {weather}\nDon't Forget to bring umbrella")



#*********************** api for weather ************************
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
weateher_paramter = {
    "lat": , # Your latitude
    "lon": , # Your longitude
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url= OWM_Endpoint, params= weateher_paramter)
response.raise_for_status()
weather_data = response.json()


will_rain = False

# to understand the list comprehension print the weather_data and paste the json data to online editor to understand how each set
weather_code = [weather_data["list"][weather_condition]["weather"][0]["id"]
                for weather_condition in range(len(weather_data) - 1)]

weather = [weather_data["list"][weather_condition]["weather"][0]["description"]
                for weather_condition in range(len(weather_data) - 1)]


weather_type = ""
for code in range(len(weather_code)):
    if weather_code[code] < 700:
        will_rain = True
        weather_type = weather[code]

if will_rain:
    send_mail(weather_type)

