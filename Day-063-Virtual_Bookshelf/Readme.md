# Day 63 – Virtual Bookshelf (Personal Library Manager)

## Project Overview

This is a personal library management web application built using Flask and SQLAlchemy. The application allows users to manage their book collection by adding new books with title, author, and rating, viewing all books in their library, and editing ratings for existing books. The project demonstrates CRUD (Create, Read, Update) operations using SQLAlchemy ORM with SQLite database. Users can add new books through a form, view the complete library at home page, and update ratings for any book they've already added. The application features a clean, simple interface with all data persistently stored in a SQLite database.

## What I Have Learned

* **SQLite Database Commands**:  Learned basic SQLite commands like CREATE TABLE to define database structure with columns and data types. For example, cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)") creates a books table with id as primary key, title as unique text field, author as text field, and rating as decimal number.

* **SQLAlchemy ORM**:  SQLAlchemy is defined as an ORM (Object Relational Mapping) library. This means it's able to map the relationships in the database into Objects. Fields become Object properties, tables can be defined as separate Classes, and each row of data becomes a new Object. This makes database operations feel like working with regular Python objects instead of writing raw SQL queries.

* **Creating a New Database**: Learned to configure SQLAlchemy to create a new SQLite database by setting SQLALCHEMY_DATABASE_URI = "sqlite:///new-books-collection.db" and initializing the app with db.init_app(app). When the application runs, SQLAlchemy automatically creates the database file if it doesn't exist.

* **Create a New Table**: Learned to define a database table by creating a class that inherits from db.Model and defining columns as class attributes. For example, class Book(db.Model) with id: Mapped[int] = mapped_column(Integer, primary_key=True) defines each column with its data type, constraints like nullable=False, unique=True, and primary_key=True.

* **Create A New Record**: Understood how to add new records to the database by creating an instance (`new_book`) of the model class (Book(title=..., author=..., rating=...)), adding it to the session with db.session.add(new_book), and committing with db.session.commit() to save permanently.

* **Read All Records**: Learned to fetch all records from a table using db.session.execute(db.select(Book).order_by(Book.title)) which returns all books sorted by title. The scalars() method converts the result into a list of model objects that can be looped through in templates.

* **Read A Particular Record By Query**: Used db.session.execute(db.select(Book).where(Book.id == book_id)).scalar() to find a specific book by its ID. The where() condition filters results, and scalar() returns a single object instead of a list.

* **Updating Records by Query and Primary Key**: Learned to update records by first fetching the specific book object using its primary key (id) from the URL like /edit?id=2. Once the book is found using db.session.execute(db.select(Book).where(Book.id == book_id)).scalar(), I can modify its rating attribute like book_to_update.rating = new_rating and commit the session with db.session.commit() to save the changes. This demonstrates how the primary key uniquely identifies a record for updates.

* **Delete A Particular Record By PRIMARY KEY**: lthough not implemented in this project, learned the concept of deleting records by fetching the object and using db.session.delete(book) followed by commit() to remove it from the database.

* **Context Management with `app.app_context()`**: Learned that database operations need to run within an application context. Used with app.app_context() to create a temporary context when performing database operations outside of route functions, ensuring the application knows which Flask app instance to use.

## How It Works

* **main.py**: The Flask application starts by importing necessary modules and setting up SQLAlchemy. The Base class inherits from DeclarativeBase and serves as the foundation for defining database models. SQLAlchemy is initialized with db = SQLAlchemy(model_class=Base), and the database URI is configured to use SQLite with the file. The `Book` class defines the database table structure with columns for id (primary key), title (string, unique, required), author (string, required), and rating (float, required). The `home route` queries all books from the database using db.session.execute(db.select(Book).order_by(Book.title)), converts the results to a list, and passes it to index.html. The `add route` handles GET requests by displaying the add form, and POST requests by extracting form data with request.form.to_dict(), calling adding_book_entry() to create and save a new Book object, then redirecting to the home page. The `edit route` captures the book ID from the URL, queries the specific book using db.session.execute(db.select(Book).where(Book.id == book_id)).scalar(), and on POST requests updates its rating and commits to the database before redirecting home.

* **adding_book_entry()**: This helper function creates a new database record. Inside with app.app_context():, it creates a Book object `new_book` using the submitted form data, and adds it to the session with db.session.add(), and commits the transaction with db.session.commit() to permanently save the book to the database.

* **index.html**: The home page template displays all books in the library. It uses Jinja's {% if books == [] %} to check if the library is empty, showing "Library is empty" message when true. Otherwise, a {% for book in books %} loop iterates through each book, displaying its title, author, and rating. Each book entry includes an "Edit Rating" link that uses {{ url_for('edit', book_id=book.id) }} to generate the edit URL with the book's ID as a query parameter.

* **add.html**: This template contains a simple form that submits to the add route using the POST method. It collects book name, author, and rating through input fields and sends them to the server when the "Add Book" button is clicked.

* **edit.html**: This template is responsible for editing the existing rating first this template displays the current book title and rating before allowing the user to enter a new rating. The form action uses {{ url_for('edit', book_id=update_book_rating.id) }} to submit the new rating to the `edit route` with the correct book ID. The input field collects the new rating and submits it via POST.

* **Database Operations**: All database operations follow a consistent pattern query using db.session.execute() with select() and optional where() conditions, fetch results using scalar() or scalars(), modify attributes as needed, and always call db.session.commit() to save changes. The application context ensures SQLAlchemy knows which app instance to use for database connections.


## Project Highlights

* **SQLAlchemy ORM**: Learned to use SQLAlchemy as an Object Relational Mapper to interact with the database using Python objects instead of raw SQL queries.
* **Database Creation**: Created SQLite database automatically with proper table structure defined through Python classes.
* **Create Records**: Learned how to Add new book entries by creating Book objects and committing them to the database.
* **Read Records**: Queried all books from the database with sorting by title using db.select(Book).order_by(Book.title).
* **Query by ID**: Learned how to retrieve specific books using where() conditions to find records by their primary key.
* **Update Records**: Learned ot modify how to update the existing data inside the database.

