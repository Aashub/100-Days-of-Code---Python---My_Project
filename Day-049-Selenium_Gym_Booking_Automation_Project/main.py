# required library
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

GYM_URL =  os.environ["gym_url"]
ACCOUNT_EMAIL =   os.environ["my_email"]
ACCOUNT_PASSWORD =  os.environ["my_password"]
ALREADY_BOOKED_WAITLISTED = 0
CLASSES_BOOKED = 0
WAITLIST_JOINED = 0
DAYS_LIST = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
CLASS_BOOKED_TITLE = []

# Configure Selenium to stay opened using the Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Creates a folder path to store Chrome browser data (cookies, login, settings) so Chrome remembers sessions
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# telling chrome driver to use this directory to store a "profile". That way every time when we quit Chrome and re-run the Selenium script, it keeps all the preferences and settings from the profile.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# running Selenium through chrome browser to open gym website
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
driver.implicitly_wait(2)

# ************************** Check Booking *******************************

def display_verification_result(confirmed_bookings, waitlist_section, total_booked):
    """this function will display the verification result that booked classes are matching or mismatching."""

    expected_bookings = len(total_booked)
    found_bookings = len(confirmed_bookings) + len(waitlist_section)

    if (expected_bookings - found_bookings) == 0:
        print(f"\n--- VERIFICATION RESULT ---\nExpected: {expected_bookings} bookings\nFound: {found_bookings} bookings\n✅ SUCCESS: All bookings verified!")

    elif (expected_bookings - found_bookings) != 0:
        print(
            f"\n--- VERIFICATION RESULT ---\nExpected: {expected_bookings} bookings\nFound: {found_bookings} bookings\n❌ MISMATCH: Missing {expected_bookings - found_bookings} bookings!")

def verify_my_classes(confirmed_bookings_obj, waitlist_section_obj, total_booked_classes):
    """this for loop will verify the booked classes in my booking section that they are matching or not. """

    class_title_list = []
    booked_class = []

    print("--- VERIFYING ON MY BOOKINGS PAGE ---\n")

    for classes in total_booked_classes: # this for loop will remove the duplicate value of classes
        if classes not in booked_class:
            booked_class.append(classes)

    for booking in confirmed_bookings_obj:  # this for loop will find all the selenium object of class title tag
        class_title_text_obj = booking.find_elements(By.CSS_SELECTOR, value="h3")

    for booking in waitlist_section_obj:  # this for loop will find all the selenium object of class title tag
        waitlist_text_obj = booking.find_elements(By.CSS_SELECTOR, value="h3")

    for class_name in class_title_text_obj:  # this for loop will use the class_title_text_obj and find the class title.

        if class_name not in class_title_list:
            class_title_list.append(class_name.text)

    for waitlist in waitlist_text_obj:  # this for loop will use the class_title_text_obj and find the class title.

        if waitlist not in class_title_list:
            class_title_list.append(waitlist.text)

    for verifying_class_name in booked_class: # this for loop will verify the booked classes vs booking showing in confirmed booking section
        for class_name in class_title_list:

            if verifying_class_name == class_name:
                print(f" ✓ Verified: {class_name}")
            else:
                class_n = class_name.split(" (Waitlist)")[0]
                if verifying_class_name == class_n:
                    print(f" ✓ Verified: {class_name}")

    display_verification_result(confirmed_bookings_obj, waitlist_section_obj, total_booked_classes)


def check_my_booking(classes_title):
    my_bookings = driver.find_element(By.ID, value= "my-bookings-link")
    my_bookings.click()

    day_list = []
    booking_page = driver.find_element(By.ID, value = "my-bookings-page")

    try:

        booking_state = booking_page.find_element(By.ID, value= "empty-bookings-state")
        booking_state_id = booking_state.get_attribute("id")

        if booking_state_id == "empty-bookings-state": # if no booking found than this will get implemented
            print("no booking_yet")

    except:
        confirmed_bookings = booking_page.find_elements(By.CSS_SELECTOR, value= "div[id^='booking-card-booking']") # for confirmed booking
        waitlist_section = booking_page.find_elements(By.CSS_SELECTOR, value="div[id^='waitlist-card-waitlist']") # for waitlist section

        for booking in confirmed_bookings:        # this for loop will find all the selenium object of p tag & class title tag
            paragraph_text_obj = booking.find_elements(By.CSS_SELECTOR, value= "p")

            for find_day in paragraph_text_obj:    # this for loop will use the paragraph_text_obj and find the booked day and store that day in a list.
                day = find_day.text.split(" ")[1]
                if day not in day_list:
                    day_list.append(day)
                    break

        for waitlist in waitlist_section:        # this for loop will find all the selenium object of p tag
            paragraph_text_obj = waitlist.find_elements(By.CSS_SELECTOR, value= "p")

            for find_waitlist in paragraph_text_obj:    # this for loop will use the paragraph_text_obj and find the waitlist day and store that day in a list.
                day = find_waitlist.text.split(" ")[1]

                if day in day_list:
                    pass
                elif day not in day_list:
                    if day in DAYS_LIST:
                        day_list.append(day)
                        break

    string = ""
    for day in day_list:  # this for loop will create a string of all booked day
        day_without_comma = day.strip(",")
        string += f"{day_without_comma}/"
    print(f"\n--- Total {string} classes: {len(day_list)} ---\n")

    try:
        verify_my_classes(confirmed_bookings, waitlist_section, classes_title)

    except UnboundLocalError:
        print("No Gym class found!")

# ************************** Make Booking *******************************

def detailed_class_details(day_date_details, class_titles, class_times):
    """this function will give a DETAILED CLASS LIST of all bookings"""
    global CLASS_BOOKED_TITLE

    print(f"\n--- DETAILED CLASS LIST  ---\n")
    for day_date in day_date_details:
        for index in range(len(class_titles)):
             if class_titles[index] == "Spin Class" and class_times[index] == "6:00 PM":
                print(f"• [New Booking] {class_titles[index]} on {day_date}")
                CLASS_BOOKED_TITLE.append(class_titles[index])

             elif class_titles[index] == "Yoga Class" and class_times[index] == "5:00 PM":
                 print(f"• [New Waitlist] {class_titles[index]} on {day_date}")
                 CLASS_BOOKED_TITLE.append(class_titles[index])


def class_booked_summary(booked_classes, joined_waitlist, already_booked_waitlisted):
    """this function will give a summary of all bookings"""

    total_classes = booked_classes + joined_waitlist + already_booked_waitlisted
    print(f"\n--- BOOKING SUMMARY ---\nClasses booked: {booked_classes}\nWaitlists entries: {joined_waitlist}\nAlready booked/waitlisted: {already_booked_waitlisted}\nTotal classes processed: {total_classes}")


def check_button_text(book_text):
    """this function checks that button status is booked or waitlisted or not and return value as per that."""

    if book_text == "Booked" or book_text == "Waitlisted":
        return 0
    else:
        return 1

def book_class(booking_details_dict, day_date_details_li):
    """this function will actually book the specific gym class on the day which we want to book that at specific time"""

    global CLASSES_BOOKED, WAITLIST_JOINED

    iterate  = 0
    for booking_day_object in booking_details_dict:

        class_titles = booking_details_dict[booking_day_object]["class_title"][0] # class_title list
        class_time = booking_details_dict[booking_day_object]["class_timing"][0] # class_time list
        class_card = booking_details_dict[booking_day_object]["class_card"][0] # class_card list

        for index in range(len(class_titles)):

            # if class title and time matches than it will implement
            if (class_titles[index] == "Spin Class" and class_time[index] == "6:00 PM") or (class_titles[index] == "Yoga Class" and class_time[index] == "5:00 PM"):

                get_button = driver.find_element(By.CSS_SELECTOR, value=f"div[id^='{class_card[index]}']")
                book_button = get_button.find_element(By.CSS_SELECTOR, value="button")

                if book_button.text.lower() == "book class": # if new class needs to be booked
                    book_button.click()
                    time.sleep(2)
                    button_text_status = check_button_text(book_button.text)

                    if button_text_status == 0:
                        print(f"✓ Successfully {book_button.text}: {class_titles[index]} on {day_date_details_li[iterate]}")
                        CLASSES_BOOKED += 1
                        return 0

                    elif button_text_status == 1:
                        return 1

                elif book_button.text.lower() == "join waitlist": # if need to join a waitlist
                    book_button.click()
                    time.sleep(2)
                    button_text_status = check_button_text(book_button.text)
                    if button_text_status == 0:
                        print(f"✓ Joined {book_button.text} for: {class_titles[index]} on {day_date_details_li[iterate]}")
                        WAITLIST_JOINED += 1
                        return 0
                    elif button_text_status == 1:
                        return 1

        iterate += 1

    class_booked_summary(CLASSES_BOOKED, WAITLIST_JOINED, ALREADY_BOOKED_WAITLISTED)
    detailed_class_details(day_date_details_li, class_titles, class_time)

    return "classes_get_booked"

def check_already_present_booking(booking_details_dict, day_date_details_li):
    """this function will check are their already present booking present or not."""

    global ALREADY_BOOKED_WAITLISTED
    already_present_class = 0
    iterate = 0
    for booking_day_object in booking_details_dict:

        class_titles = booking_details_dict[booking_day_object]["class_title"][0]  # class_title list
        class_time = booking_details_dict[booking_day_object]["class_timing"][0]  # class_time list
        class_card = booking_details_dict[booking_day_object]["class_card"][0]  # class_card list

        for index in range(len(class_titles)):

            # if class title and time matches than it will implement
            if (class_titles[index] == "Spin Class" and class_time[index] == "6:00 PM") or (class_titles[index] == "Yoga Class" and class_time[index] == "5:00 PM"):

                get_button = driver.find_element(By.CSS_SELECTOR, value=f"div[id^='{class_card[index]}']")
                book_button = get_button.find_element(By.CSS_SELECTOR, value="button")

                if book_button.text.lower() == "booked":  # if class is already booked by you
                    print(f"✓ Already {book_button.text}: {class_titles[index]} on {day_date_details_li[iterate]}")
                    ALREADY_BOOKED_WAITLISTED += 1
                    already_present_class += 1

                elif book_button.text.lower() == "waitlisted":  # if waitlist is already joined by you
                    print(f"✓ Already {book_button.text}: {class_titles[index]} on {day_date_details_li[iterate]}")
                    ALREADY_BOOKED_WAITLISTED += 1
                    already_present_class += 1

        iterate += 1

    if already_present_class > 0:
        class_booked_summary(CLASSES_BOOKED, WAITLIST_JOINED, ALREADY_BOOKED_WAITLISTED)
    else:
        pass

def retrying_booking_class(booking_detail_dict, day_date_detail_li):
    """this function retry the booking until the booking doen't happen in case if booking didin't happen for some reason like network error."""

    global  ALREADY_BOOKED_WAITLISTED
    retry = 10
    attempt = 1
    should_continue = True

    check_already_present_booking(booking_detail_dict, day_date_detail_li)

    if ALREADY_BOOKED_WAITLISTED > 0:
        return None

    else:
        while should_continue:
            print(f"Trying Booking. Attempt: {attempt}")
            button_clicked_status = book_class(booking_detail_dict, day_date_detail_li)

            if retry == attempt:
                print("All attempt used.")

            if button_clicked_status == 0:
                attempt = 1

            elif button_clicked_status == 1:
                attempt += 1

            elif button_clicked_status == "classes_get_booked":
                should_continue = False


def selecting_booking_day(booking_day_id_li, day_date_details_li):
    """this function will create a dictionary of all the booking class details of each day in form of list like class_card, class_title, class_timing & return dictionary and day_date_list"""

    booking_day_id_dict = {day_group:{"class_card": [], "class_title": [], "class_timing": []} for day_group in booking_day_id_li}

    for booking_day_object in booking_day_id_dict:

        # this will create a list of class_card in a dictionary of all classes which have all details of each classes of that day.
        class_card = booking_day_object.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")
        booking_day_id_dict[booking_day_object]["class_card"].append([card.get_attribute("id") for card in class_card])

        # this will create a list of all class title list in a dictionary of that specific day.
        class_title = booking_day_object.find_elements(By.CSS_SELECTOR, value="h3")
        booking_day_id_dict[booking_day_object]["class_title"].append([h.text for h in class_title])

        # this will create a list of all classes timing list in a dictionary of that specific day.
        class_timing = booking_day_object.find_elements(By.CSS_SELECTOR, value="p[id^='class-time-']")
        booking_day_id_dict[booking_day_object]["class_timing"].append([time.text.split("Time: ")[1] for time in class_timing])

    # book_class(booking_day_id_dict, day_date_details_li)

    return booking_day_id_dict, day_date_details_li

def find_ancestor_div_element(card_sib_element):
    """this function will help in get the ancestor/parent div tag and day and date list of specific day of which we want to book a class."""

    day_store_list = []
    booking_day_id_list = []
    day_date_list = []
    for child in card_sib_element:

        ancestor_div = child.find_element(By.XPATH, value="..")
        day_title_obj = ancestor_div.find_element(By.TAG_NAME, value="h2")

        booking_day = ancestor_div.get_attribute("id")
        day_title = day_title_obj.text

        # if any id has monday or tuesday or any mentioned day which we want it will store that id in day_store_list list & day date data in list day_date_list.
        if "mon" in booking_day or "tue" in booking_day:
            if booking_day not in day_store_list:
                day_store_list.append(booking_day)
                day_date_list.append(day_title)

    for day in day_store_list: # this for loop will give the selenium object of each day.

        booking_day_id = driver.find_element(By.ID, value=day)
        booking_day_id_list.append(booking_day_id)

    return booking_day_id_list, day_date_list

# ***************************************************************

# clicking on login button
login_button = driver.find_element(By.ID , value = "login-button")
login_button.click()


def login():
    """this function will fill all the required login details in the page."""

    # entering email id
    enter_email = driver.find_element(By.ID, value="email-input")
    enter_email.clear()
    enter_email.send_keys(ACCOUNT_EMAIL)

    # entering password
    enter_password = driver.find_element(By.ID, value="password-input")
    enter_password.clear()
    enter_password.send_keys(ACCOUNT_PASSWORD)

    # clicking on submit button
    submit_button = driver.find_element(By.ID, value="submit-button")
    submit_button.click()

    time.sleep(2)
    current_url = driver.current_url
    if "https://appbrewery.github.io/gym/login/" ==  current_url:
        return 1
    else:
        print("Login Successful!")
        return 0


def retry(retries):
    """this function will call the login wrapper function multiple times until login didn't happen"""

    for attempt in range(1, retries):

        print(f"Trying login. Attempt: {attempt}")
        verify_login = login()

        if verify_login == 0:
            break
        elif verify_login == 1:
            pass
        if attempt == retries:
            print("All retries failed")

retry(retries=10)


# card_sibling_element will hold the list of all the elements which has id of class-card-
card_sibling_element = driver.find_elements(By.CSS_SELECTOR , value = "div[id^='class-card-']")

# function will give the parent div tag id in which their child tag have all class details
booking_id_list, day_date_li = find_ancestor_div_element(card_sibling_element)

# selecting booking day
booking_details_dict, day_date_details_li = selecting_booking_day(booking_id_list, day_date_li)

# this function make sure that class get booked even network fails happen how much time.
retrying_booking_class(booking_details_dict, day_date_details_li)

# checking my booking classes
check_my_booking(CLASS_BOOKED_TITLE)
















