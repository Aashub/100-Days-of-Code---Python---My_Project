# Day 51 - Internet Speed Twitter Complaint Bot

## Project Overview

This is an Internet Speed Test and Twitter Complaint Automation bot built using Selenium WebDriver and undetected-chromedriver. The script automatically checks your internet download and upload speeds using Speedtest.net, compares them against your promised speeds, and if the actual speeds are lower than promised, it automatically logs into Twitter (X) and posts a complaint tweet tagging your internet service provider. The bot handles complex Twitter login flows including email/username verification, password entry, and handles cases where Twitter asks for additional verification (email/phone). This project was created using Selenium WebDriver, undetected-chromedriver, explicit waits, retry logic, and environment variables for secure credential storage.

## What I Learned

* Multi-website automation: Learned how to coordinate automation across two different websites (Speedtest.net and Twitter.com) in a single workflow.
* Undetected ChromeDriver: Used the undetected_chromedriver library to avoid being flagged as a bot by Twitter's anti-automation systems.
* Dynamic waiting strategies: Combined WebDriverWait with expected conditions and fixed time.sleep() delays to handle elements that appear after unpredictable loading times.

## How It Works

### Main
* **Speed Test Execution:** First it creates an instance of InternetSpeed than it Implements a retry loop (while button_click) that repeatedly calls retry_until() function until the accepting_condition button is successfully clicked. than it calls get_internet_speed() method to retrieve download and upload speeds after that it  Quits the Speedtest browser driver
* **Conditional Twitter Posting:** In this part of code first it Compares actual speeds against promised speeds (PROMISED_DOWNLOAD=200, PROMISED_UPLOAD=25), If both download AND upload speeds are lower than promised speed of internet, than it proceeds with Twitter automation first it Creates a Twitter_login instance after it calls the click_sign_in() method to initiate login and reach to the sign in page after reaching to the sign in page than it calls retry_sign_in() function with intelligent retry logic and it Runs a while loop attempting login via sign_in() method if return value of sign_in() method is `email_window` than it waits a random interval (5-10 seconds) and retry again for sign_in by calling sign_in() method if return value comes out as `login_successful` than it exit the while loop and calls create_post() method with promised and actual speed values so that it can create and publish post than it Quits the Twitter browser driver.

### InternetSpeed Class
* **__init__():** Initializes the Chrome WebDriver with the detach option to keep the browser open after script completion. Navigates to Speedtest.net and sets an implicit wait of 2 seconds for element discovery.
* **accepting_condition():** Attempts to locate and click the cookie consent popup using XPath targeting the "Accept" button. If the button is found and clicked, it returns "button_clicked". If the button is not found (meaning no popup appeared), it returns "button_not_clicked". This return value is used by the retry mechanism in the main script.
* **get_internet_speed():** Locates and clicks the "Go" button (start-text class) to begin the speed test. Waits for 90 seconds using time.sleep() to allow the test to complete. After completion, extracts the download and upload speed values using CSS selector targeting span elements with class starting with result-data-large. Stores these values in instance variables self.down and self.up and returns them as a variable.

### Twitter_login Class 
* **__init__():** Initializes undetected ChromeDriver with specific version matching (version_main=145) to avoid version mismatch errors. if everything goes find than it Navigates to Twitter.com and sets up WebDriverWait with a 20-second timeout.
* **click_sign_in():** This method Locates all div elements with a specific CSS class pattern and clicks the second element (index 1) which corresponds to the "Sign in" button on Twitter's homepage.
* **sign_in():** This is the main login logic used to sign in the twitter account first it Clicks into the email/username input field and then it Clears any existing text and enters the Twitter username from environment variables than it Clicks the "Next" button after that it waits for some second and checks the text of a specific span element to determine what Twitter is asking for next, If it asks for "Enter your phone number or email address", than it calls method of verify_details() enter_password() and returns "login_successful", If it asks for "Enter your password", directly calls enter_password() and returns "login_successful", If neither condition matches, returns "email_window" to trigger a sign_in() method again.
* **verify_details():** Handles the case where Twitter needs additional verification (email/phone) details first it Clicks into the input field than it Enters the email ID from environment variables after that i tClicks the "Next" button to proceed to password entry.
* **enter_password():** This method complete teh login process first it Clicks into the password input field than Enters the password from environment variables than Clicks the "Log in" button to complete authentication.
* **create_post():** This method is used to create and publish the complaint tweet first it Locates and clicks the "Post" (feather) button to open the tweet composer, than it Waits 2 seconds for the composer to load than Locates the message input area and sends a formatted tweet containing the promised vs actual speeds of download and upload speed than it  Locates and clicks the "Post" button to publish the tweet.

## Project Highlights

*  **Cross-Platform Automation**: Seamlessly integrates automation across two completely different websites (Speedtest.net and Twitter.com).
*  **Undetected Browser Automation**: Uses undetected-chromedriver to bypass Twitter's anti-bot protections and maintain successful logins.
*  **Complex Login Handling**: Successfully navigates Twitter's multi-step login flow that sometimes requires email/phone verification in addition to username/password
*  **Flexible Element Selection**: Mastered multiple selector strategies (CSS prefixes, XPath, class names, tag names) to handle dynamically generated elements across different websites.
* **Human-like Behavior**: Uses random delays and retry patterns to mimic human interaction patterns and avoid detection