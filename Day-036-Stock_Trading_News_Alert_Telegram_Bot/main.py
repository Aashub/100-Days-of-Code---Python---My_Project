from datetime import datetime, timedelta
import requests
from twilio.rest import Client

def send_mail(arti_list, percentage):
    """this function will will send the all three article message on telegram using telegram bot api."""

    emoji_sign = ""
    if percentage > 0:
        emoji_sign = "🔺"
    elif percentage < 0:
        emoji_sign = "🔻"

    news = ""
    # this for loop will format all news article message in a proper way.
    for news_letter in arti_list:
        news += f"{percentage}%{emoji_sign}\n{news_letter[0]}\n\nHeadline: {news_letter[1]}\n\nBrief: {news_letter[2]}\n\n\n"

    parameters = {
        "chat_id": "",
        "text": f"Stock news alert\n\n{news}"

    }

    BOT_TOKEN = ""
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.get(url = telegram_url, params= parameters)
    response.raise_for_status()
    message_data = response.json()


def get_recent_news(yest, day_before_yest):
    """this function will find the most relevant stock news for the company as per the provided keyword of the company for ex: Reliance Industries and return news data"""

    news_api_key = ""
    news_parameters = {
        "q": '("Reliance Industries" OR "RIL" OR "Mukesh Ambani" OR "reliance industries")',
        "from": day_before_yest,
        "to": yest,
        "sortBy": "publishedAt",
        "apiKey": news_api_key
    }

    news_url = "https://newsapi.org/v2/everything"
    response = requests.get(url=news_url, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()

    return news_data


today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_date = str(yesterday.date())
yesterday_name = yesterday.strftime("%A")

# this if condition will prevent us to get the sunday and saturday stock data because in our json stock_data sunday and saturday dates get skipped so it will let us skip those days.
if yesterday_name == "Sunday":
    yesterday = today - timedelta(days=3)
    yesterday_date = str(yesterday.date())
    yesterday_name = yesterday.strftime("%A")

day_before_yesterday = yesterday - timedelta(days=1)
day_before_yesterday_date = str(day_before_yesterday.date())
day_before_yesterday_name = day_before_yesterday.strftime("%A")

if day_before_yesterday_name == "Sunday":
    day_before_yesterday = yesterday - timedelta(days=3)
    day_before_yesterday_date = str(day_before_yesterday.date())
    day_before_yesterday_name = day_before_yesterday.strftime("%A")


stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": "RELIANCE.BSE",
    "outputsize": "compact",
    "apikey": ""
}

# this api will help us to know that how much stock percentage has gone up or gone down
url = 'https://www.alphavantage.co/query'
response = requests.get(url= url, params= stock_parameters)
response.raise_for_status()
stock_data = response.json()

yest_closing_price = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
day_before_yest_closing_price = float(stock_data["Time Series (Daily)"][day_before_yesterday_date]["4. close"])

percentage_change = (yest_closing_price - day_before_yest_closing_price)/day_before_yest_closing_price * 100


if 5 >= percentage_change <= 5:
   news_data = get_recent_news(yesterday_date, day_before_yesterday_date)

# this for loop will filter out most relevant reliance company news based on the provided keywords
article_list = []
for news in news_data["articles"]:

    article_title = news["title"]
    article_description = news["description"]
    article_url = news["url"]
    article_tuple = (article_url, article_title, article_description)
    if ("reliance industries" in article_description.lower() or "ril" in article_description.lower() or "mukesh ambani"
            in article_description.lower()):
        article_list.append(article_tuple)

    if len(article_list) > 2:
        break


send_mail(article_list, round(percentage_change,2))




