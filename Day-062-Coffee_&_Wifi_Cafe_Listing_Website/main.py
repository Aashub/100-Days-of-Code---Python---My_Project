from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["secret_key"]  # secret key
Bootstrap5(app)

# this class will use FLaskForm to create a desired fields for the form
class CafeForm(FlaskForm):
    Cafe_Name = StringField('Cafe name', validators=[DataRequired()])
    Location = URLField('Cafe Location on Google Map(URL)', validators=[DataRequired(), URL()])
    Open = StringField('Opening Time e.g.(8:00 AM)', validators=[DataRequired()])
    Close = StringField('Closing Time e.g.(5:30 PM)', validators=[DataRequired()])
    Coffee = SelectField('coffee rating',
                         choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
                         validators=[DataRequired()])
    Wifi = SelectField('Wifi rating',
                       choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                                ('💪💪💪💪💪', '💪💪💪💪💪')],
                       validators=[DataRequired()])
    Power = SelectField('Power Outlet rating',
                        choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                 ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                        validators=[DataRequired()])

    submit = SubmitField('Submit')


# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():    # render home page
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():     # render add_cafe form page if request method is get and render all cafes page if request method is post.
    form = CafeForm()

    if request.method == "GET":  # if request.method condition comes out true this is statment will come out true.
        return render_template('add.html', form=form)

    elif request.method == "POST":  # once the form is filled and user clicks on login button this condition will become true.

        if form.validate_on_submit():

            if form.submit.data == True:

                field_names = [column_title for column_title in form.data if
                               column_title != "submit" and column_title != "csrf_token"]       # list comprehension is used to prevent extra column to be added in the csv file like submit and csrk_token

                # here we are updating a csv file with new data.
                with open(file=f"cafe-data.csv", mode="a", newline='', encoding='utf-8') as csv_file:
                    csv_data = csv.DictWriter(csv_file, fieldnames=field_names, extrasaction='ignore')
                    csv_data.writerow(form.data)

                return cafes()


@app.route('/cafes')
def cafes():    # this will render all cafes page

    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
