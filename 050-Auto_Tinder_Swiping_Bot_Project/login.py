# library
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

TINDER_URL = "https://tinder.com/"
EMAIL_ID =  os.environ["my_email"]
PHONE_NO =  os.environ["phone_no."]

# Create an undetected Chrome driver instance
chrome_option = uc.ChromeOptions()

# Creates a folder path to store Chrome browser data (cookies, login, settings) so Chrome remembers sessions
profile_path = os.path.join(os.getcwd(), "chrome_profile")


driver = uc.Chrome(user_data_dir = profile_path, options= chrome_option)
wait = WebDriverWait(driver, 20)

driver.get(TINDER_URL)


class Tinder:

    def __init__(self):

        # for current tab
        self.main_tab = driver.current_window_handle

    def accept_agreement(self):
        """this method will accept the agreement on tinder page"""

        agree_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "w1u9t036")))

        for accept_agreement in range(len(agree_buttons)): # this for loop  will loop in all the tags which has class Id w1u9t036 and if that class id text matches than it will click and accept the conditions.

            if agree_buttons[accept_agreement].text.lower() == "i accept":
                agree_buttons[accept_agreement].click()
                break

    def click_login(self):
        """this method will click on login button on tinder page"""

        login_button = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lxn9zzn")))


        for button in range(len(login_button)):  # this method will loop in all the tags which has class Id w1u9t036 and if that class id text matches than log in button clicked.

            if login_button[button].text.lower() == "log in":
                login_button[button].click()
                break

    def click_google_button(self):
        """this function will click on google button"""

        try:
            google_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nsm7Bb-HzV7m-LgbsSe-BPrWId")))
            google_button.click()

            # to get all tabs objects
            all_tabs = driver.window_handles
            return all_tabs

        except: # to return None value
                return None

    def enter_email(self):
        """this function will enter the email ID in the new opened tab"""

        # enter_email = driver.find_element(By.TAG_NAME, value = "input")
        enter_email = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        enter_email.send_keys(EMAIL_ID)


    def enter_phone_number(self):
        """this method will enter the phone number in tinder for verification"""

        enter_phone_num = wait.until(EC.presence_of_element_located((By.ID, "phone_number")))
        enter_phone_num.send_keys(PHONE_NO)

        click_next = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lxn9zzn")))

        for clicking in click_next:

            if clicking.text == "Next":
                print(clicking.text)
                clicking.click()
                break

    def allow_location(self):
        """this method will click on allow location pop up"""

        allow_location = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lxn9zzn")))
        print(allow_location.text)
        allow_location.click()

    def turn_on_notification(self):
        """this method will turn on notification when pop up appears"""

        allow_notification = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lxn9zzn")))
        print(allow_notification.text)
        allow_notification.click()

    def right_swipe(self):
        """this function will make a right_swipe on a profile"""

        make_right_swipe = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class^='button Lts($ls-s)']")))

        for right_swipe in range(len(make_right_swipe)):

            if right_swipe == 4:
                make_right_swipe[right_swipe].click()
                break

    def check_maximum_swipe_exceed(self):
        """this function will check that if maximum swipe exceeded than it will close the program"""

        cross_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class^='C($c-ds-icon-secondary-inverse)']")))
        cross_button.click()