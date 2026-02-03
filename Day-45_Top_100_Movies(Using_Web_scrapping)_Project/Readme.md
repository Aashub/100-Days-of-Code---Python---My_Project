# Day 45 – Top 100 Movies Web Scraping Project

## Project Overview

This project is a Python-based web scraping project where I learned how to extract data from a real website using Python libraries Bs4. In this project, I scraped the list of the top 100 movies of all time from a movie ranking webpage and saved the extracted data into a text file. The main goal of this project was to understand how web scraping works, how HTML elements are structured on a webpage and how to find the required data using inspect method, and how to collect useful information programmatically.

## What I Have Learned

* **Web Scraping**: Learned what web scraping is and how it allows us to extract useful data from websites by reading and analyzing their HTML structure.
* **Finding Multiple Elements**: Learned how to use `soup.find_all(name="a")` method to collect multiple HTML elements of the same type from a webpage.
* **Extracting Text and Links**: Learned how to extract text using `tag.getText()` and links using `tag.get("href")` from HTML tags.
* **Finding Specific Elements**: Learned how to locate specific elements using `soup.find(name="h3", class_="title")` when both tag name and class are required.

## How It Works

* **Requesting the Webpage**: The `requests.get()` method is used to request the webpage and fetch its HTML content.
* **HTML Parsing:**: The webpage content is passed into BeautifulSoup with the "html.parser" to make the HTML searchable.
* **Data Extraction**: Movie titles are extracted using soup.find_all(name="h3", class_="title").
* **Data Cleaning**: Movie names are cleaned using split() to remove ranking numbers and extra characters.
* **List Creation:**: All extracted movie titles are stored in a Python list in the correct order.
* **File Generation**: The final list is written into a .txt file named top_100_movies.txt, displaying the top 100 movies.

## Project Highlights

* Learned the basics of web scraping using Python
* Learned how to extract and clean real-world data from HTML.


