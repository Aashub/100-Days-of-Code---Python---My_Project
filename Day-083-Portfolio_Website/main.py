from flask import Flask, render_template, request
import requests


def send_mail(message_data) :
    """this function will create the secure connection between sender and receiver using smtp module and take input of weather condition and send the mail."""

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: New Message! \n\n{message_data}")


app = Flask(__name__)


@app.route('/')
def home():
    """the decorator and this function will help in render the home page of website."""

    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True, port= 6001)