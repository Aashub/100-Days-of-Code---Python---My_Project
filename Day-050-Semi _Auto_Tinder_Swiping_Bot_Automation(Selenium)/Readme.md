# Day 50 - Selenium Semi Auto Tinder Swiping Bot Automation 

## Project Overview

This is a Tinder Semi automation bot built using Selenium and undetected-chromedriver. The script semi automates the entire login process via Google, handles phone number verification, allows location and notification permissions, and then continuously performs right swipes on each tinder profiles. Also it  monitors for the “maximum swipe limit reached” and when pop-up appears than it gracefully exit when the limit is hit. The bot is also designed to bypass basic detection by using a persistent Chrome profile to maintain session state across runs so after the chrome profile created and whenever the user runs the program it doesn't need to login it automatically opens the tinder website and started right swiping.

## What I Learned

* **Undetected ChromeDriver:** Used the undetected_chromedriver library to avoid being flagged as a bot by Tinder’s anti‑bot mechanisms.
* **Multi‑tab handling:** Learned how to switch between browser tabs during Google OAuth login and return to the main Tinder tab by using `driver.switch_to.window()` method.
* **Session persistence:** Learned how to store Chrome user data in a local folder so that cookies and login state are preserved between runs, so that next time when program runs it doesn't need to re‑authenticate and just started swiping.

## How It Works

* **Top‑level control flow:** The script first tries to accept the agreement and click the login button. If the Google login button is found, it handles the multi‑tab Google authentication (email entry) and then waits for the user to manually type “continue” to signal that they have completed any remaining steps on the Google page (like password entry). After that, it enters the phone number, and then waits for the user to type “allow” to permit location and notification permissions. Finally, it enters the swiping loop.
* **`accept_agreement()`:** this method Locates all elements with class `w1u9t036` in the browser and clicks the one with the text “I accept” to accept Tinder’s terms of service. This handles the initial agreement overlay.
* **`click_login()`:** Finds all elements with class `lxn9zzn` and clicks the one with the text `“Log in`. This opens the login options modal.
* **`click_google_button()`:** This method Waits for the Google login button (identifiable by a complex class name used by Google’s Sign‑In button) to become clickable and clicks it. Returns a list of all window handles after the click. If the button is not found (e.g., because the user is already logged in via the profile), it returns None. This return value is used to decide whether to handle the Google login flow or proceed directly to swiping
* **`enter_email()`:** Switches to the newly opened Google login tab and enters the email address into the first `<input>` field. The email is taken from the environment variable my_email.
* **`enter_phone_number()`:** After returning to the main Tinder tab, this method locates the phone number input field (by ID phone_number) and enters the phone number from the environment variable phone_no.. Then it finds the “Next” button (again by class lxn9zzn) and clicks it.
* **`allow_location()`:** When the browser asks for location permission, this method clicks the “Allow” button (located using class lxn9zzn).
* **`turn_on_notification()`:** Similar to allow_location() method, this method clicks on the “Allow” button for the notifications permission pop‑up so that it get closed and we also get notification.
* **`right_swipe()`:** This method Performs a right swipe on a tinder profile. It finds all buttons with a CSS selector targeting the swipe‑action buttons (button[class^='button Lts($ls-s)']) and clicks the fifth button (index 4), which corresponds to the “Like” (right swipe) button.
* **`check_maximum_swipe_exceed()`:** This method is used for stopping the swiping and exit the program so when maximum swipe limit reached the tinder gives us the pop that maximum swipe limit reached at that time this function got triggered and it clicks on the close button (identified by a CSS selector targeting the cross icon). This stops the swiping loop when the daily limit is hit and exit the code.
* **`implement_right_swiping()`:** This top‑level function manages the main swiping loop. It repeatedly calls right_swipe() method so that right swipe happened on tinder  profiles until the “maximum swipe exceeded” pop‑up appears. When that pop‑up is detected, check_maximum_swipe_exceed() method closes it and the loop exits. After exiting, the driver is quit.

## Limitations

*  the reason why it is semi automatic is because google don't allow us to login using selenium automation method because if we try to login we used to get pop up of `This browser of app may not be secured` that's why i have decided to make this bot semi automatic.    

## Project Highlights

*  **Undetected ChromeDriver**: learned how to use undetected_chromedriver to mimic a real browser so that i don't face any issue while trying to login using selenium.

  