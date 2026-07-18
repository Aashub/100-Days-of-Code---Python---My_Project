# required imports
from flask import Flask, render_template, request, session, redirect, url_for
import requests
import os
from github_graph import GithubData
from smtplib import SMTP
from email.message import EmailMessage

#Environment variables
EMAIL = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
PER_EMAIL = os.environ["PER_EMAIL"]
SECRET_KEY = os.urandom(24).hex()


# calling the Github Class to fetch github required data to create a contribution graph
fetch_data = GithubData()
response_status = fetch_data.checking_response()

# if response status is 0 than it will call the required method to get the required details
if response_status == 0:
    repo_count, overall_stars, overall_forks, overall_contribution = fetch_data.fetching_required_data()
    graph_contribution_list, month_label_list = fetch_data.fetch_month_labels()

    response_list = [repo_count, overall_stars, overall_forks, overall_contribution]

# else show the error.
elif response_status == 1:
    print("please check the above error")



def send_mail(message_data_dict):
    """this function will create the secure connection between sender and receiver using smtp module and take input from contact page send the mail."""

    msg = EmailMessage()


    msg["Subject"] = message_data_dict["subject"]
    msg["From"] = EMAIL
    msg["To"] = PER_EMAIL
    msg["Reply-To"] = message_data_dict["email"]
    msg.set_content(message_data_dict["message_content"])

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=password)

        connection.send_message(msg)


app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/', methods=['GET'])
def home():
    """the decorator and this function will help in render the home page of website."""

    return render_template("index.html", contribution_highlights=response_list,
                           contribution_graph=graph_contribution_list, num_of_weeks=len(graph_contribution_list),
                           months_label=month_label_list)


@app.route('/projects', methods=['GET'])
def projects():
    """this decorator will help in render projects page."""

    return render_template("projects.html")


@app.route('/about_me', methods=['GET'])
def about_me():
    """this decorator help in render about me page."""

    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """this route is responsible for rendering the contact page and fetch the data of the user who wants to reach out to me."""

    if request.method == 'POST':
        message_data_dict = {

            "name": request.form['name'],
            "email": request.form['email'],
            "subject": request.form['subject'],
            "message_content": request.form['message']

        }

        send_mail(message_data_dict)

        # Setting a temporary flag in the session

        session['mail_sent'] = True
        return redirect(url_for('contact'))  # once the message sent successful this will render contact.html page and show succesful sent message

    # Check if the flag exists in the session
    show_success = session.pop('mail_sent', False)

    return render_template("contact.html", show_success = show_success)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
