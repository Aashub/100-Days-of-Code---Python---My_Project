# Day 53 – Web Scrapping Data Entry Project

## Project Overview

This project is a Python-based web scraping and automation project that extracts rental property data from Zillow and automatically submits it to a Google Form. It uses BeautifulSoup for web scraping purpose on the other hand it usees Selenium for form filling automation, this bot collects apartment listing details including addresses, prices, and links from a Zillow search page, then systematically fills and submits each entry into a Google Form. The main goal of this project was to combine web scraping techniques with browser automation to create a seamless data collection and submission pipeline.

## What I Have Learned

* **Selenium Form Automation**:Learned how to automate Google Form filling by locating input fields dynamically and handling different field types sequentially.
* **Exception Handling in Automation**: Implemented specific exception handling for StaleElementReferenceException and ElementNotInteractableException to make the automation more robust.

## How it works

* **Zillow Data Scraping with BeautifulSoup**: The bot first sends a GET request to the Zillow URL stored in environment variables. Using BeautifulSoup, it parses the HTML response and extracts three types of data: property links by finding all anchor tags with class "property-card-link", apartment prices by locating span elements with class "PropertyCardWrapper__StyledPriceLine" and cleaning them by removing "+/mo" text, and apartment addresses by finding all address tags and stripping extra whitespace and newlines. All three datasets are stored in separate lists with matching indices.
* **Google Form Initialization:**: Selenium WebDriver is configured with Chrome options that keep the browser open after script completion (detach=True). The driver navigates to the Google Form URL stored in environment variables and sets an implicit wait of 2 seconds to ensure elements load properly before interaction.
* **Main Submission Loop:**: The bot enters a while loop that continues until all apartment listings are processed. At the start of each iteration, it verifies it's on the correct form page by checking for the form title "SF Renting Research". It then calls fill_input_fields() with the current index. If successful, it locates and clicks the submit button (the second submit element), waits for confirmation, and verifies successful submission by checking for the "Your response has been recorded." message. After verification, it increments the counter and reloads the form for the next entry. If any exceptions occur during form filling, it reloads the form and retries the current entry.
* **fill_input_fields()**: The fill_input_fields() function takes the current iteration number as a parameter and handles the actual form filling process. It first finds all input fields on the Google Form using a CSS selector targeting Google Forms' dynamic class pattern. For each field (index 0, 1, 2), it sends the corresponding data - address, price, and link - from the scraped lists. The function includes try-except blocks specifically for StaleElementReferenceException and ElementNotInteractableException, returning appropriate error messages if retry is needed, or "details_filled" upon successful completion.
* **Completion Condition**: The loop continuously checks if the current index has reached the total number of scraped addresses. Once all entries are processed, should_continue is set to False and the bot stops, having successfully submitted all rental listings to the Google Form.

## Project Highlights

* learned how to implement specific exception handlers for common Selenium issues like stale elements and non-interactable elements
* Successfully combined BeautifulSoup for data extraction and Selenium for form submission automation in a single workflow




