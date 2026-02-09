# Day 48 – Cookie Clicker Game Bot Using Selenium

## Project Overview

This project is a Python-based browser automation project where I learned how to automate a real website using Selenium WebDriver. In this project, I automated the Cookie Clicker game by continuously clicking the cookie, checking available cookies, analyzing upgrade prices, and automatically buying the best possible upgrade at regular time intervals. The main goal of this project was to understand how browser automation works, how to interact with webpage elements, and how to make decisions dynamically based on live website data.

## What I Have Learned

* **Selenium WebDriver**:Learned what Selenium WebDriver is and how it allows us to automate real browsers like Chrome using Python.
* **Finding Elements on a Webpage**: Finding Elements on a Webpage, `find_element(By.CLASS_NAME)`, `find_element(By.NAME)`, `find_element(By.ID)`, `find_element(By.CSS_SELECTOR)`, `find_element(By.XPATH)`.
* **Working With Web Elements**: Learned how to extract text from elements using .text and manipulate the extracted data for logic building.
* **Filling Input Fields and Clicking Buttons**: Learned how to fill input fields using .send_keys() method and Learned how to submit forms or press buttons using Keys.ENTER.

## What I Have Learned

* **Launching the Browser**: Selenium WebDriver is used to open Chrome and load the Cookie Clicker website.
* **Language Selection:**: After the page loads it give us the option of language selection for playing the game after it waits for 10 seconds so that by that time all things load up properly so that no value error happens and language element get selected for the game.
* **Cookie Clicking Automation**: In while loop The main cookie is continuously clicked using .click() method  in order to generate a cookies continuously.
* **Upgrade Price Handling**: Every 5 seconds, the script checks different bulk-buy options (1, 10, 100) each bulk-buy option call `check_buy_item()` function which will extract current cookie count from the webpage and convert them into usable numeric values for comparison with the upgrades values in order to buy them. Also so same function is used to cleaning upgrade price value if they have ',', ' million' and ' billion' in their value so that upgrade buy comparison happens properly. 
* **Best Upgrade Selection**: After we get the data of current cookies and highest upgradable item it buys the most expensive upgradable item.    
* **Performance Tracking**: After 5 minutes, the script prints how many cookies are being generated per second and stops execution.

## Project Highlights

* Learned real-world browser automation using Selenium
* Learned how to interact with dynamic web elements and extract data from it.
* Learned about different finding methods of element on a web browser using Selenium like f`ind_element(By.CLASS_NAME)`, `find_element(By.NAME)`, `find_element(By.ID)`, `find_element(By.CSS_SELECTOR)`, `find_element(By.XPATH)` and also Filling Input Fields and Clicking Buttons.