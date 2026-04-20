import os
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["secret_key"]


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["db"]
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Flask-Login class
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)  # Returns actual User object


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


# Getting the instance folder path
instance_path = Path(app.instance_path)
db_path = instance_path / 'users.db'


def create_database():
    # Checking if the database file exist or not as per that new database will be created
    if not db_path.exists():
        with app.app_context():
            db.create_all()

        print(f'Database created successfully!')

    else:
        try:
            print(f'Database already exists at:, {db_path}')
            print(f'Skipping creation.')

        except OSError:
            pass


@app.route('/')
def home():
    create_database()

    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """this route renders register.html page and in post request adds email, pwd, and username in database and authenticate user so he gets logged in."""

    if request.method == 'POST':

        entered_email = request.form.get('email')
        user_obj = db.session.execute(db.select(User).where(User.email == entered_email)).scalar()

        if user_obj:

            flash("You've have already signed up with that email, log in Instead!")
            return redirect("login")

        else:

            not_hash_pwd = request.form.get('password')
            hashed_salted_pwd = generate_password_hash(not_hash_pwd, method='pbkdf2:sha256', salt_length=8)

            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hashed_salted_pwd,
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)  # Log in and authenticate user after adding details to database.
            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """this route renders login page and in post request do authentication and that user provided correct email or password or not."""

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        user_obj = db.session.execute(db.select(User).where(User.email == email)).scalar()

        # Handle non-existent email_id
        if not user_obj:
            flash("That Email, does not exist. Please try again!")
            return render_template("login.html")

        else:  # if email_id exist.
            pwd_hash = user_obj.password

            status = check_password_hash(pwd_hash,
                                         password)  # it will check the stored hash password with plain text password using this method and return True if correct password provided.
            if status:
                login_user(user_obj)
                return redirect(url_for("secrets"))

            else:
                flash("Password Incorrect. Please try again!")
                return render_template("login.html")

    return render_template("login.html")


# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    """this route renders the secrets.html page."""

    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    """this route will logout the user and redirect to the home page."""

    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    """this route responsible for rendering pdf file page."""

    return send_from_directory('static', path='files/cheat_sheet.pdf', as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
