# required library
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap4
import os

EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]


# flask_wtf form class for login page
class LoginForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(message="Invalid email address."), Length(min=5, max=64)])
    Password = PasswordField('Password', validators=[DataRequired(message="Field must be 8 characters long."),
                                                     Length(min=8, max=64)])
    login = SubmitField('Login')


app = Flask(__name__)
bootstrap = Bootstrap4(app)

app.config['SECRET_KEY'] = os.environ["secret_key"]  # csrf secret key required if want to use the FLASK form and make secure connection


@app.route("/")
def home():
    """this will load the home page."""
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    """this will load the login page"""

    form = LoginForm()
    if request.method == "GET":  # if request.method condition comes out true this is statment will come out true.

        return render_template("login.html", login_form=form)

    elif request.method == "POST":   # once the form is filled and user clicks on login button this condition will become true.

        if form.validate_on_submit(): #submit validation

            if EMAIL == form.Email.data and PASSWORD == form.Password.data:
                return render_template("success.html")

            else:
                return render_template("denied.html")

        return render_template("login.html", login_form=form)


if __name__ == '__main__':
    app.run(debug=True)
