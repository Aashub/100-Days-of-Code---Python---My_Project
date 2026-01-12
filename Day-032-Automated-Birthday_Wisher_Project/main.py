import pandas
import random
from smtplib import SMTP
import datetime as dt

def send_mail(birthday_let):
    """this function will create the secure connection between sender and receiver using smtp module and take input of birthday letter."""

    my_email = "@gmail.com"
    password = "jiwvmkgqvdmooxdu"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person_email,
                            msg=f"Subject: Happy Birthday! \n\n{birthday_let}")

num = random.randint(1, 3)

# here we are reading the csv file of the birthday person details and storing their required details in the variable.
birthday_file = pandas.read_csv("birthdays.csv")

birthday_person_details = birthday_file[birthday_file.name == "Asteroid Destroyer"]
birthday_person_name = birthday_person_details.name.item()
day_of_birth  = birthday_person_details.day.item()
month_of_birth = birthday_person_details.month.item()
birthday_person_email = birthday_person_details.email.item()

# here we are using datetime module to get the current date so that user check the birthday date with the current date.
now = dt.datetime.now()
current_day = now.day
current_month = now.month

if day_of_birth == current_day and month_of_birth == current_month:

    # here we are reading the random letter template and replacing place_holder[NAME] with the birthday person name
    with open(f"letter_templates/letter_{num}.txt") as letter_file:
        letter_format = letter_file.read()
        birthday_letter = letter_format.replace("[NAME]", birthday_person_name)

send_mail(birthday_letter)








