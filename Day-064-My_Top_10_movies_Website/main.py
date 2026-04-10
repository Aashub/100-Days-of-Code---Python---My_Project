from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import FloatField
from wtforms.validators import DataRequired
import requests
import os
from pathlib import Path


API_ACCESS_TOKEN = os.environ["api_access_token"]
API_KEY = os.environ["api_key"]


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["secret_key"]
Bootstrap5(app)

# CREATE DB
# Create Base class for SQLAlchemy ORM
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the Base class
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-details-database.db"  # configure the SQLite database, relative to the app instance folder
db.init_app(app)  # initialize the app with the extension


# this class will use FLaskForm to create a desired fields for the form
class EditMovieForm(FlaskForm):
    new_rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])

    submit = SubmitField('Done')

# this class will use FLaskForm to create a desired fields for the form
class AddMovieForm(FlaskForm):

    new_movie = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# CREATE TABLE
# Define your model - must be after db.init_app(app)
class Movie(db.Model):
    __tablename__ = "movie_details"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Getting the instance folder path
instance_path = Path(app.instance_path)
db_path = instance_path / 'movies-details-database.db'

def create_database():

    # Checking if the database file exist or not as per that new database will be created
    if not db_path.exists():
        with app.app_context():
            db.create_all()

        # print(f'Database created successfully!')

    else:

        try:
            print(f'Database already exists at:, {db_path}')
            print(f'Skipping creation.')

        except OSError:
            pass

def update_rating_review(movie_form, movie_to_update):
    """this function will validate the movie form data and update the new rating review data in database"""

    if movie_form.validate_on_submit():
        if movie_form.submit.data == True:

            movie_to_update.rating = movie_form.data["new_rating"]
            movie_to_update.review = movie_form.data["new_review"]
            db.session.commit()

    # print("review/rating updated in database successfully")


def fetch_themoviedb_url_and_headers(movie):
    """this function will return url and headers for making movie search requests"""

    url = f"https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": API_ACCESS_TOKEN
    }

    return url, headers

def update_movie_data_in_database(movie_id):
    """this function make a get request using movie_id to get the selected movie details like title, poster image, ratings, and update those data in database."""

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": API_ACCESS_TOKEN
    }

    response = requests.get(url, headers=headers)
    movie = response.json()

    with app.app_context():
        new_movie = Movie(title = movie["title"], year = movie["release_date"], description = movie["overview"], img_url = movie["poster_path"])
        db.session.add(new_movie)
        db.session.commit()

        # print("New Movie added in database successfully!")
        movie_id = new_movie.id

        return movie_id


def update_ranking(all_movies):
    # this function will be responsible for the updating the ranking of the movies.

    for index, movie_details in enumerate(all_movies):

        with app.app_context():
            ranking_to_update = db.session.execute(db.select(Movie).where(Movie.title == movie_details.title)).scalar()
            ranking_to_update.ranking = None
            db.session.commit()

    ranking_list = [movie.rating for movie in all_movies]

    for index, rating in enumerate(reversed(ranking_list)):

        with app.app_context():
            ranking_to_update = db.session.execute(db.select(Movie).where(Movie.rating == rating)).scalar()
            ranking_to_update.ranking = index + 1
            db.session.commit()

    return redirect(url_for('home'))

@app.route("/")
def home():
    """this function will render the home page with existing books all details"""
    all_movies = []
    create_database()  # calls create_database function

    # Check for movie_id from clicked link (GET request)
    movie_id = request.args.get('movie_id')
    if movie_id:
        id = update_movie_data_in_database(movie_id)
        return redirect(url_for('edit_rating_review', movie_id = id))

    with app.app_context():

        movie_data = db.session.execute(db.select(Movie).order_by(Movie.rating))     # here we are reading the old movies data so we can use them.
        movies = movie_data.scalars()
        [all_movies.append(movie) for movie in movies]

        update_ranking(all_movies)
        return render_template("index.html", all_movies = all_movies)


@app.route('/edit?/id=<int:movie_id>', methods=['GET', 'POST'])
def edit_rating_review(movie_id):
    """this function will be responsible for calling edit.html page and fetching the movie_form data and calling update_rating_review() function"""

    edit_movie = EditMovieForm()

    with app.app_context():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_title = movie_to_update.title

        if request.method == 'POST':         # if request is POST than it will by fetching the new data of rating from request.form it will update the new rating.

            update_rating_review(edit_movie, movie_to_update)   # function calling for updating review rating in database

            return redirect(url_for('home'))

        elif request.method == 'GET':        # if request is GET it will render the edit page
            return render_template("edit.html", form = edit_movie, movie_title = movie_title)


@app.route('/delete/id=<int:movie_id>')
def delete_movie(movie_id):
    """this function will be responsible for the deleting a particular movie which was requested by user."""

    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_movie():

    add_new_movie = AddMovieForm()

    if request.method == 'GET':
        return render_template("add.html", form = add_new_movie)

    elif request.method == 'POST':
        if add_new_movie.validate_on_submit():
            movie_name = add_new_movie.data["new_movie"]

            URL, headers = fetch_themoviedb_url_and_headers(movie_name)

            # print(f"url: {URL}, \nheader: {headers}")

            response = requests.get(url = URL, headers=headers)
            searched_movie_data = response.json()

            return render_template("select.html", searched_movie_data = searched_movie_data)


if __name__ == '__main__':
    app.run(debug=True)
