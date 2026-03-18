from flask import Flask, render_template, request
import requests
from smtplib import SMTP
import os

EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
BLOG_ENDPOINT = "https://api.npoint.io/1937bc8b8e40c31b0db0"


blog_response = requests.get(url=BLOG_ENDPOINT)
blog_data = blog_response.json()


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

    return render_template("index.html",  all_blog_post = blog_data)


@app.route("/<string:page>" , methods = ["GET","POST"])
def show_page(page):
    """this function will help in render different pages like home, about and contact page. of blog website"""

    if page == "home":
        return render_template("index.html", all_blog_post=blog_data)

    elif page == "about":
        return render_template("about.html")

    elif page == "contact" and request.method == "GET":
        return render_template("contact.html")

    elif request.method ==  "POST":     # if this condition become true than it will call the send_mail function for sending message
        name = request.form['name']
        email = request.form['email']
        phone_no = request.form['phone']
        message = request.form['message']

        message_data = f'Name: {name}\nEmail: {email}\nPhone_no: {phone_no}\nMessage: {message}'

        send_mail(message_data)

        msg = "successful"
        return render_template("contact.html", successful_msg = msg)  # once the message sent successful this will render contact.html page and show succesful sent message


@app.route("/<int:num>")
def show_blog(num):
    """this function will help in render the blog post page when user clicks on the title & subtitle."""

    return render_template("post.html", all_blog_post= blog_data , post_num=num)


if __name__ == "__main__":
    app.run(debug=True, port= 5002)
