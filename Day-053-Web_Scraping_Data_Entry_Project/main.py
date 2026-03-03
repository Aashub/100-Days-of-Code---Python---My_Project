import time
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.by import By

ZILLOW_URL = os.environ["zillow_url"]
GOOGLE_FORM_URL = os.environ["google_form_url"]

# **************** Using BeautifulSoup to get data from the website *******************

response = requests.get(ZILLOW_URL)
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, "html.parser")

# getting links
page_links = soup.find_all(name = "a", class_ = "property-card-link")
link_list = [element.get("href") for element in page_links]

# getting prices
apartment_prices = soup.find_all(name= "span", class_ = "PropertyCardWrapper__StyledPriceLine")
apartment_price_list = [price.text.strip("+/mo") for price in apartment_prices]

# getting addresses
apartments_addresses = soup.find_all(name= "address")
apartment_address_list = [address.text.strip("\n \n") for address in apartments_addresses]

# **************** Using Selenium to Fill the Form *******************

# Configure Selenium to stay opened using the Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# running Selenium through chrome browser to open gym website
driver = webdriver.Chrome(options = chrome_options)
driver.get(GOOGLE_FORM_URL)
driver.implicitly_wait(2)


def fill_input_fields(current_iterate_num):
    """this function will fill the details in the forms and return if details get filled successfully and return error msg if something went wrong for try again."""

    # this will check how many fields are present in the page as per that amount loop will run to fill details
    fill_details = driver.find_elements(By.CSS_SELECTOR, value="input[class^='whsOnd zHQkBf']")
    for entry in range(len(fill_details)):

        try:
            if entry == 0:
                fill_details[entry].send_keys(apartment_address_list[current_iterate_num])

            elif entry == 1:
                fill_details[entry].send_keys(apartment_price_list[current_iterate_num])

            elif entry == 2:
                fill_details[entry].send_keys(link_list[current_num])

        except StaleElementReferenceException:
            print("retrying")
            return "StaleElementReferenceException"

        except ElementNotInteractableException:
            print("retrying")
            return "ElementNotInteractableException"

    return "details_filled"

current_num = 0
should_continue = True
while should_continue: # while loop runs until length of apartment_address_list is dont become equal to current iterate num.

    time.sleep(2)
    check_form_page = driver.find_element(By.CSS_SELECTOR, value="div[class^='F9yp7e ikZYwf LgNcQe']")  # to check that are we in form page or not.
    if check_form_page.text == "SF Renting Research":

        check_details_filled = fill_input_fields(current_num)

        if check_details_filled == "details_filled":
            submit = driver.find_elements(By.CSS_SELECTOR, value = "span[class^='NPEfkd RveJvd snByac']") # if details got filled it will select the submit button and clicks on it.
            submit[1].click()

            time.sleep(2)
            verify_response = driver.find_element(By.CLASS_NAME, value="vHW8K") # it will check that response is getting submitted successfully or not.
            if verify_response.text == "Your response has been recorded.":

                print(f"response {current_num + 1} submitted successfully")
                driver.get(GOOGLE_FORM_URL)
                current_num += 1

        elif check_details_filled in ["StaleElementReferenceException", "ElementNotInteractableException"]:
            driver.get(GOOGLE_FORM_URL)
            pass

    if len(apartment_address_list) == current_num:
        should_continue = False

