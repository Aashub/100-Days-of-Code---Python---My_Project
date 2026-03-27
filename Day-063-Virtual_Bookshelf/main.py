from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# how to use SQLAlchemy to create a database

# Create Base class for SQLAlchemy ORM
class Base(DeclarativeBase):
    pass


# Initialize SQLAlchemy with the Base class
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"  # configure the SQLite database, relative to the app instance folder
db.init_app(app)  # initialize the app with the extension


# Define your model - must be after db.init_app(app)
class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


def adding_book_entry(books):
    """this function job is to add new book data into the Database."""

    with app.app_context():
        new_book = Book(title=books["book_name"], author=books["book_author"], rating=books["book_rating"])
        db.session.add(new_book)
        db.session.commit()

    print("Database tables created successfully!")


@app.route('/')
def home():
    """this function will render the home page with existing books all details"""

    all_books = []

    with app.app_context():
        result = db.session.execute(
            db.select(Book).order_by(Book.title))  # here we are reading the old book data so we can use them.
        books = result.scalars()

        [all_books.append(book) for book in books]

        return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """this function will render the new book add page and when user fills the book details also it will call adding_book_entry function."""

    if request.method == 'GET':  # rendering add page.
        return render_template("add.html")

    elif request.method == 'POST':

        all_books = request.form.to_dict()
        adding_book_entry(all_books)  # calling this function

        return redirect(url_for('home'))


@app.route('/edit?/id=<float:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    """this function job is to edit the rating of the requested book."""

    with app.app_context():

        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        if request.method == 'POST':  # if request is POST than it will by fetching the new data of rating from request.form it will update the new rating.

            book_to_update.rating = request.form["book_rating"]
            db.session.commit()

            return redirect(url_for('home'))

        elif request.method == 'GET':  # if request is GET it will render the edit page
            return render_template("edit.html", update_book_rating=book_to_update)


if __name__ == "__main__":
    app.run(debug=True)
