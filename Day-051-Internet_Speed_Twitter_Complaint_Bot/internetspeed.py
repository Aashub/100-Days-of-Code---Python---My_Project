from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SPEED_TEST_WEBSITE = "https://www.speedtest.net/"

class InternetSpeed():

    def __init__(self):

        # Configure Selenium to stay opened using the Chrome option
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        # running Selenium through chrome browser
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(SPEED_TEST_WEBSITE)
        self.driver.implicitly_wait(2)


    def accepting_condition(self):
        """this method will accept condition"""

        try:

            accept_condition = self.driver.find_element(By.XPATH, value="//*[@id='onetrust-accept-btn-handler']")
            print(accept_condition.text)
            accept_condition.click()
            return "button_clicked"

        except:
            return "button_not_clicked"

    def get_internet_speed(self):
        """this method will help us in getting internet download and upload speed"""

        check_speed = self.driver.find_element(By.CLASS_NAME, value = "start-text")
        check_speed.click()

        time.sleep(90)
        internet_speed = self.driver.find_elements(By.CSS_SELECTOR, value="span[class^='result-data-large']")

        self.down = internet_speed[0].text
        self.up = internet_speed[1].text

        return self.down, self.up





