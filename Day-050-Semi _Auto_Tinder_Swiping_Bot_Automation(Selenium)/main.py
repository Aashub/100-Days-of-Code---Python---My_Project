from login import Tinder, driver

tinder = Tinder()

def implement_right_swiping():
    """this function will implement right swipe until the condition doesn't become false"""

    should_continue = True
    while should_continue:

        try:
            tinder.check_maximum_swipe_exceed()  # this method will check & close the pop of maximum right swipe exceeded
            should_continue = False

        except:
            tinder.right_swipe()

    print("maximum attempt exceeded program exited")
    driver.quit()

try:
    tinder.accept_agreement()
    tinder.click_login()
    all_tabs = tinder.click_google_button()
except:
    all_tabs = tinder.click_google_button()

# all_tabs value will be None then this if statement get implemented
if all_tabs == None:
    implement_right_swiping()

# else this one get implemented
else:
    for tab in all_tabs: # this for loop will switch the tab for google login

        if tab != tinder.main_tab:
            driver.switch_to.window(tab)
            break

    # # entering email
    tinder.enter_email()

    switch_tab = True
    while switch_tab:
        user_input = input("enter continue to switch the tab for the driver").lower()

        if user_input == "continue":
            driver.switch_to.window(tinder.main_tab)
            tinder.enter_phone_number()

            for_location = True
            while for_location:
                user_input = input("enter allow to allow the location in the browser").lower()

                if user_input == "allow":
                    tinder.allow_location()

                    driver.implicitly_wait(2)
                    tinder.turn_on_notification()

                    implement_right_swiping()
                    for_location = False
                else:
                    print("Incorrect Input, Please try again")
            switch_tab = False

        else:
            print("Incorrect Input, Please try again")

