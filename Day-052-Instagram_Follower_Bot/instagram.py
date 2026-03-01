import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


# login credential
INSTA_USER_ID = os.environ["user_id"]
PASSWORD = os.environ["password"]
INSTAGRAM_WEBSITE = "https://www.instagram.com/"
REQUEST_SEND_COUNT = 0

class Instagram():

    def __init__(self):

        # Configure Selenium to stay opened using the Chrome option
        self.chrome_option = uc.ChromeOptions()

        ############# keep this thing in check that chrome version and chrome driver version should match otherwise Win 6 error you will get #######################
        self.driver = uc.Chrome(version_main = 145, options=self.chrome_option)
        self.wait = WebDriverWait(self.driver, 20)

        self.driver.get(INSTAGRAM_WEBSITE)

    def login(self):
        """this method is used for login into the instagram"""

        # this will enter the username and password in the input field
        enter_credentials = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[class^='x1i10hfl xggy1nq xtpw4lu x1tutvks x1s3xk63']")))
        enter_credentials[0].send_keys(INSTA_USER_ID)
        enter_credentials[1].send_keys(PASSWORD)

        # this will click on the login button
        click_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class^='x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51']")))
        click_login.click()

        # this will click on not save login info button
        save_login_info = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class^='x78zum5 xdt5ytf x1e56ztr']")))
        save_login_info.click()


    def search_page(self):
        """this method job is to search the page in the instagram and clicks on it."""

        # this will click on search button
        time.sleep(4)
        click_search_option = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='x9f619 xxk0z11 xii2z7h']")))
        click_search_option[4].click()

        # this will enter keyword in search field.
        time.sleep(4)
        search = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        search.send_keys("animespotlight")

        # this will click on the desired page which we are looking for.
        time.sleep(4)
        select_page = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class^='x1lliihq x1plvlek xryxfnj x1n2onr6 xyejjpt x15dsfln x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f']")))
        select_page[0].click()


    def find_followers(self):
        """this method main job is to find followers and clicks on them for following."""

        global REQUEST_SEND_COUNT
        time.sleep(4)

        # this will click on the follower count.
        click_followers_count = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class^='x5n08af x1s688f']")))
        click_followers_count[1].click()

        should_be_greater = True
        while should_be_greater:

            time.sleep(4)  # this will loop for the all the follow request button after the window get opened.
            send_follow_requests = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='_ap3a _aaco _aacw _aad6 _aade']")))

            for button in send_follow_requests[1:]:

                time.sleep(2)
                button_text = button.text

                if REQUEST_SEND_COUNT == 20: # if request send count is become 20 it will ask the user do you want to continue

                    should_continue = True
                    while should_continue:
                        user_input = input(f"You've sent {REQUEST_SEND_COUNT} requests. Continue? (yes/no): ")

                        if user_input.lower() == "yes":
                            REQUEST_SEND_COUNT = 0
                            should_continue = False

                        elif user_input.lower() == "no":
                            return None
                        else:
                            print("invalid input, Please try again")
                else:
                    is_action_successful = self.retry_again(button_text, button)

                    if is_action_successful:
                        pass


    def retry_again(self, button_tx, btn):
        """this method job is to keep retry clicking on follow button until the button register get successful."""

        global REQUEST_SEND_COUNT
        should_continue = True
        while should_continue:
            try:
                if button_tx == "Follow":
                    REQUEST_SEND_COUNT += 1
                    print(REQUEST_SEND_COUNT)
                    btn.click()

                elif button_tx == "Following" or button_tx == "Requested":
                    time.sleep(2)
                    btn.click()
                    unfollow_popup = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class^='_a9-- _ap36 _a9_1']")))
                    time.sleep(2)
                    unfollow_popup.click()

            except:
                print("Error has occurred, try again")

            else:
                should_continue = False

        return True









