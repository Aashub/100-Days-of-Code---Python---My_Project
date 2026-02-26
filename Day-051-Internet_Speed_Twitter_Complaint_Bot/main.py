from internetspeed import InternetSpeed
from twitterbot import Twitter_login
import time
import random

PROMISED_DOWNLOAD = 200
PROMISED_UPLOAD = 25

# *****************************for to get Internet speed ***************************

internet_speed = InternetSpeed()

def retry_until():
    """this function will run until accepting_condition() function don't accept the condition"""

    accept_cond = internet_speed.accepting_condition()
    return accept_cond

button_click = True
while button_click:

    output_value = retry_until()
    if output_value == "button_clicked":
        button_click = False
    elif output_value == "button_not_clicked":
        pass

download_speed, upload_speed = internet_speed.get_internet_speed()
internet_speed.driver.quit()


# *****************************for Twitter Post***************************

if PROMISED_DOWNLOAD > float(download_speed) and PROMISED_UPLOAD > float(upload_speed):

    twitter = Twitter_login()

    def retry_sign_in():
        """this function is used so that login attempt happen again and again until the twitter don't get signed in."""

        should_continue = True
        while should_continue:
            to_check = twitter.sign_in()

            if to_check == "email_window": # if the return value is email_window than this if statement generate a random second for next retry
                time.sleep(random.randint(5, 10))
                pass

            elif to_check == "login_successful": # if login is successful than here we will exit the while loop.
                should_continue = False

        twitter.create_post(PROMISED_DOWNLOAD, PROMISED_UPLOAD, download_speed, upload_speed)
        twitter.driver.quit()

    twitter.click_sign_in()
    retry_sign_in()
