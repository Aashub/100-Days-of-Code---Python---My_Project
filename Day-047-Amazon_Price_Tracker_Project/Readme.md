# Day 47 – Amazon Price Tracker Project

## Project Overview

This project is a Python-based web scraping project where I learned how to track the price of a product on Amazon and get notified through email when the price drops below a certain value. In this project, I used Python libraries like requests, BeautifulSoup, and smtplib to scrape product information from an Amazon product page, process the extracted data, and send an automated email alert. The main goal of this project was to understand how web scraping works with email notifications.

## What I Have Learned

* **Web Scraping on Real Websites**: Learned how to send HTTP requests with custom headers to scrape data from a real website like Amazon without getting blocked immediately.
* **Data Cleaning & Processing**: Learned how to clean extracted text data by removing commas, extra spaces, and unwanted characters and convert prices into integers for comparison.

## How It Works

* **Requesting the Product Page**: The requests.get() method is used along with custom request headers to fetch the Amazon product page HTML.
* **HTML Parsing:**: The webpage HTML is passed into BeautifulSoup using the "html.parser" to make the content searchable.
* **Price Extraction**: The product price is extracted using soup.find_all() and cleaned by removing commas and decimals.
* **Price Comparison:**: The current product price is compared with a predefined lowest price.
* **Email Alert System:**: If the current price is lower than the set limit, the send_mail() function is triggered and an email alert is sent automatically.
* **Secure Email Sending**: The SMTP connection uses TLS encryption to securely send the email.

## Limitations

* I tried to scrape prices from Indian Amazon product pages (amazon.in), but due to strict restrictions and anti-bot measures on the Amazon website, I was not able to extract the required data reliably. Even after using custom request headers, the website blocked or returned incomplete responses, which made it difficult to build a proper price tracking system using web scraping alone.
* I learned that there is a legitimate way to overcome this limitation by registering as an Amazon Associate and using Amazon’s Product Advertising API. However, to get access to this API, an Associates account must first generate a minimum number of qualified sales (currently 10 sales within 30 days). Only after meeting this requirement can the API be used to build a fully functional and reliable Amazon price tracking system. This approach is the only ethical and officially supported way to access Amazon product data.



