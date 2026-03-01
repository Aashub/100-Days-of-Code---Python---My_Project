# Day 52 - Instagram Follower Bot

## Project Overview

This is an Instagram Follower Automation Bot built using Selenium WebDriver and undetected-chromedriver. The script automatically logs into your Instagram account, searches for a specific page (animespotlight), opens its followers list, and begins sending follow requests to users. The bot includes intelligent retry logic, handles both following and unfollowing actions, and implements a request counter that pauses after every 20 follow requests to ask for user confirmation before continuing. This project was created using Selenium WebDriver, undetected-chromedriver, explicit waits, retry mechanisms, and environment variables for secure credential storage.

## What I Learned

* **Dynamic Element Selection**: Practised CSS selector prefixes (^=) to target elements with dynamically generated class names that change but maintain consistent prefixes on Instagram.
* **Complex Navigation Flows**: Learned how to navigate through Instagram's multi-step process - login → search → select page → access followers → interact with follow buttons.
* **Retry Logic Implementation**: Created a dedicated retry method that handles failed click attempts and continues execution without crashing the entire script.

## How It Works

### Main Execution Flow

* **Instance Creation**: First it creates an instance of the Instagram class which initializes the undetected ChromeDriver
* **Sequential Execution**:  Calls the three main methods in sequence - login(), search_page(), and find_followers()
* **Error Handling**: Wraps the entire execution in a try-except-finally block to catch any exceptions and ensure the browser driver quits properly
* **Cleanup**: Always executes driver.quit() in the finally block to close the browser even if errors occur

### Instagram Class

* **init()**: First what it does is Browser Configuration, Initializes undetected ChromeDriver with specific version matching (version_main=145) to avoid version mismatch errors (critical for avoiding WinError 6), than it creates Wait Setup: Creates a WebDriverWait instance with 20-second timeout for reliable element detection than it Navigates directly to Instagram's homepage (https://www.instagram.com/
* **login()**: This method handles the complete Instagram authentication process. It first locates both username and password input fields simultaneously using a CSS selector that targets elements with specific class prefixes, then sends the credentials retrieved from environment variables. After entering credentials, it finds and clicks the login button using another complex CSS selector matching Instagram's dynamic class structure. Finally, it handles the "Save your login info?" popup that appears after successful login by locating and clicking the appropriate button, completing the authentication flow.
* **search_page()**: This method manages the navigation to the target Instagram profile. It begins with a 4-second delay to mimic human behavior, then locates and clicks the search icon (the fourth element in a list of navigation elements). After another 4-second pause, it finds the search input field by its tag name and types "animespotlight" as the search keyword. Following a final 4-second delay to allow search results to load, it locates the specific search result containing the target page using a detailed CSS selector and clicks on it to navigate to the profile page.
* **find_followers()**: This method contains the core follower interaction logic. It starts with a 4-second delay, then clicks on the follower count element (the second element in a list of count displays) to open the followers list popup. The method enters a while loop that continues indefinitely, collecting all follow/unfollow buttons within the popup using a CSS selector targeting the button pattern. For each button (skipping the first one which is typically the "Followers" header), it retrieves the button text and checks the global REQUEST_SEND_COUNT. When the count reaches 20, it pauses and asks the user whether to continue - if "yes", it resets the counter and proceeds; if "no", it exits the method entirely. For each button, it calls the retry_again() method to handle the actual click action, passing the button text and the button element itself.
* **retry_again()**: This method provides robust error handling for follow/unfollow actions through a retry mechanism. It enters a while loop that continues until the action is successfully completed. If the button text is "Follow", it increments the global REQUEST_SEND_COUNT, prints the current count, and clicks the button. If the button text is "Following" or "Requested", it clicks the button to initiate unfollow, waits for the confirmation popup to appear, locates the confirmation button using a CSS selector, and clicks it to complete the unfollow process. The entire operation is wrapped in a try-except block - if any exception occurs during clicking, it prints an error message and the while loop continues to retry. Only when the action completes without error does the loop exit and the method return True.
