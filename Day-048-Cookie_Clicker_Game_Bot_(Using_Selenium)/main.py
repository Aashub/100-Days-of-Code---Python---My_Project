# required library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# webdriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


def check_buy_item():
    """This function check all three buy section and return the buy item value"""

    product_price = [0, 1, 2]

    # cookies we have
    cookies = driver.find_element(By.ID, value="cookies")
    our_cookies = cookies.text.split(" ")[0]
    final_value = 0

    # this for loop will check all three section of item value and compare it with our cookies value and store their value in final value
    for price in product_price:
        buyable_things = driver.find_element(By.ID, value=f"productPrice{str(price)}")

        upgrade_item_value = buyable_things.text

        # if any upgrade_item_value has "," in their  value this if statement will run and remove that comma
        if "," in upgrade_item_value:
            new_value = upgrade_item_value.replace(",","")

            if int(our_cookies) > int(new_value):
                final_value = new_value

        # if any upgrade_item_value has "million" in their value this if statement will run and remove that '.' and ' million' from it
        elif "million" in upgrade_item_value:
            new_value = upgrade_item_value.replace(".","")
            trimmed_value = new_value.replace(" million", "") + "000"

            if int(our_cookies) > int(trimmed_value):
                final_value = trimmed_value

        # if any upgrade_item_value has "million" in their value this if statement will run and remove that '.' and ' billion' from it
        elif "billion" in upgrade_item_value:
            new_value = upgrade_item_value.replace(".", "")
            trimmed_value = new_value.replace(" billion", "") + "000000"

            if int(our_cookies) > int(trimmed_value):
                final_value = trimmed_value

        else:
            if int(our_cookies) > int(upgrade_item_value):
                final_value = upgrade_item_value

    return final_value


time.sleep(7)

# select language
select_language = driver.find_element(By.ID, value="langSelect-EN")
select_language.click()

#click on the cookie
click_cookie = driver.find_element(By.ID, value="bigCookie")

# this variable will help us in to check after how much time which if statement should implement after certain seconds
start_time = time.time()
five_minute = time.time()

should_continue = True
while should_continue:

    click_cookie.click()

    # if time became more than 5 secs than this statement will run
    if time.time() - start_time >= 5:

        buy_level = ["1", "10", "100"]
        final_price_list = []

        # this for loop will help in go jump through all three storeBulk upgrade buy section
        for buy in buy_level:
            stage = driver.find_element(By.ID, value = f"storeBulk{buy}")
            stage.click()

            buy_option =  int(stage.text)
            if buy_option == 1 or 10 or 100:
                final_price =  check_buy_item()
                final_price_list.append(final_price)

        # below list comprehension is used to change the list price value to integer value of all list element
        change_type_list = [int(price) for price in final_price_list]

        buy = driver.find_element(By.ID, value=f"product{str(change_type_list.index(max(change_type_list)))}")
        buy.click()

        start_time = time.time()

    # if 5 minutes completed this if statement will run and print how many cookies we are generating per second and loop breaks.
    if time.time() - five_minute >= 300:
        cookies_per_second = driver.find_element(By.ID, value=f"cookiesPerSecond")
        per_second = cookies_per_second.text.split(" ")[2]
        print(f"cookies/second: {per_second}")
        should_continue = False




