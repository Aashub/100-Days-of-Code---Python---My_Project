# required library
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

# twitter login constant
TWITTER_USERNAME = os.environ["user_name"]
TWITTER_EMAIL_ID = os.environ["email_id"]
TWITTER_PASSWORD = os.environ["password"]
TWITTER_WEBSITE = "https://x.com/"

class Twitter_login():
    def __init__(self):

        # Configure Selenium to stay opened using the Chrome option
        self.chrome_option = uc.ChromeOptions()

        ############# keep this thing in check that chrome version and chrome driver version should match otherwise Win 6 error you will get #######################
        self.driver = uc.Chrome(version_main = 145,  options = self.chrome_option)
        self.wait = WebDriverWait(self.driver, 20)

        self.driver.get(TWITTER_WEBSITE)


    def click_sign_in(self):
        """this function will click on sign in button."""

        sign_in_button = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='css-146c3p1 r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q']")))
        sign_in_button[1].click()

    def sign_in(self):
        """this method get called  again and again until the entered user id accepted and we can enter to the next page of enter password or email id."""

        # this will click into the email field
        enter_in_email = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-135wba7']")))
        enter_in_email.click()

        # this will clear the existing text and fill input field with new user ID text.
        fill_email = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        fill_email.clear()
        fill_email.send_keys(TWITTER_USERNAME)

        # this will click on next button
        click_next_button = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='css-175oi2r r-xoduu5']")))
        click_next_button[2].click()

        time.sleep(4) # this will give us the text of next page
        text = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class^='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']")))
        verify_text = text[1].text

        # if verify text matches this text than this will get implemented
        if verify_text == "Enter your phone number or email address":

            self.verify_details()
            self.enter_password()
            return "login_successful"

        # if verify text matches this text than this will get implemented
        elif verify_text == "Enter your password":
            self.enter_password()
            return "login_successful"

        else:
            return "email_window"


    def verify_details(self):
        """this method will enter the email ID."""

        # this will click into the email field by clicking on it
        enter_in_email = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[class^='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-135wba7']")))
        enter_in_email.click()

        # this will enter the email Id into the input feild
        fill_email = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        fill_email.clear()
        fill_email.send_keys(TWITTER_EMAIL_ID)

        # this will click on the next button
        click_next_button = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class^='css-1jxf684 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1inkyih']")))
        print(click_next_button[0].text)
        click_next_button[0].click()


    def enter_password(self):
        """this method will enter the password and click on login button"""

        time.sleep(4)
        # this will click into the input field of password
        enter_in_password = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-135wba7']")))
        enter_in_password[1].click()

        # this will fill the input field with the password
        fill_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class^='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj']")))
        fill_password.clear()
        fill_password.send_keys(TWITTER_PASSWORD)

        # this will click on the login button
        click_login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class^='css-1jxf684 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1inkyih']")))
        click_login_button.click()

    def create_post(self, promised_download_sp, promised_upload_up, actual_download_speed, actual_upload_speed):
        """this method will create and publish a post on twitter"""

        # this will click on the feather button which will open the post window.
        click_feather_button = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class^='css-1jxf684 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1inkyih r-rjixqe']")))
        click_feather_button[1].click()

        time.sleep(2)
        # this will fill the post text with input field
        enter_message = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")))
        enter_message[0].send_keys(f"Hey @reliancejio, why is my internet speed is {actual_download_speed}download/{actual_upload_speed}upload when i pay for {promised_download_sp}download/{promised_upload_up}upload speed.")

        # this will click on post button so that post will get posted.
        post_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21']")))
        post_button.click()

        print("post send successfully")
