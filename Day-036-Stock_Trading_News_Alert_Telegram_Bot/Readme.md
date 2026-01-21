# Day 36 – Stock Trading News Alert Telegram Bot

## Project Overview

This project is a Stock News Alert Telegram Bot built using Python. The app monitors daily stock price changes for a specific company (in this case, Reliance Industries) using the Alpha Vantage API. If the stock price increases or decreases by 5% compared to the previous trading day, the program fetches relevant news articles about the company using the NewsAPI. It then automatically sends a formatted notification via Telegram to alert the user about significant stock movements and the related news. This project focuses on working with APIs and messaging via Telegram bot.

## What I Have Learned

* **API Integration**: Learned how to work with multiple APIs (Alpha Vantage and NewsAPI) and combine data from different sources for actionable insights also learned about how to find the relevant api by reading their docs and finding out which relevant api i should use to work with.

* **Nested Dictionary & JSON Handling**: Revised how to extract required information from nested JSON responses for stock data and news articles

* **Telegram Bot Messaging**: Learned to send automated, formatted messages to Telegram using the telegram Bot API.

## How It Works

* **`Alpha Vantage API`**: The program fetches daily stock data for relevant company we want it for in my case it was Reliance Industries from the Alpha Vantage API. It calculates the percentage change in closing price between yesterday and the day before yesterday. the datetime module is skip the sunday and saturday because in Alpha Vantage API the data we get it skips the sunday and saturday and only gives the data rest of the day so their are if condition who prevent it from that.

* **`get_recent_news() & NewsAPI`**: If the stock price change is ±5%, the program triggers the `get_recent_news()` function which will get called and from NEWS API fetch us the all the news data from the last two days and return that news data.

* **Fetch Relevant News**: after that the returned news_data will later be filtered out with the keywords `"Reliance Industries", "RIL", and "Mukesh Ambani"` to get the most relevant news or reliance industries using for loop appending by appending the list of tuples(url, title, description) of starting 3 article related to the stock company and store those tuple in the `article_list`

* **`send_mail()`**: This function formats the articles in a readable way and by using telegram bot api it sends a notification msg to the telegram bot which i have created.

## Limitations

* I am unable to automate the process to send the message on daily basis because in order to do that i had to buy a subscription of platform like `pypthonanywhere` which helps us to automate this process to send this kind of notification on daily basis. 

## Project Highlights

* learned how to read and find out the ways how to use this api and work with them.
* Gained hands-on experience in sending real-time notifications using Telegram bots.