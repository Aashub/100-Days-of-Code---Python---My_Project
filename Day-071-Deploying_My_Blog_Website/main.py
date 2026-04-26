from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import BlogForm, RegisterForm, LoginForm, CommentForm
import os
from pathlib import Path
from smtplib import SMTP

EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("secret_key")
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configuring Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)  # Returns actual User object


# Getting the instance folder path
instance_path = Path(app.instance_path)
db_path = instance_path / 'posts.db'


# Creating a User table for all your registered users.
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # *******Adding parent relationship*******#
    # "comment_author" refers to the comment_author property in the Comment class and "author" refers to the author property in the BlogPost class..
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

# Creating a User table for all your registered users.
class Comment(db.Model):
    __tablename__ = "comments"

    # *******Adding child relationship*******#
    # "user.id" refers to the table name of the User class and "comments" refers to the comments property in the User class.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)

# Represents a blog post entity in the database with fields for title, subtitle, publication date, content, author, and image URL.
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # ****************parent relationship *************************
    comments = relationship("Comment", back_populates="parent_post", cascade="all, delete-orphan")


# For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


def send_mail(message_data):
    """this function will create the secure connection between sender and receiver using smtp module and take input of weather condition and send the mail."""

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: New Message! \n\n{message_data}")


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


def read_blogs_data():
    """this function will read the old data from database of posts and return the blogs obj"""

    blog_data = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.id))  # here we are reading the old movies data so we can use them.
    blogs = blog_data.scalars()

    return blogs

# this decorator function will help in checking that user is admin or not.
def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return func(*args, **kwargs)

    return decorated_function


#  Using Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    """this route is responsible for rendering Register.html page. and registering the new user in the database."""

    registration_form = RegisterForm()
    if request.method == 'POST':

        if registration_form.validate_on_submit() and registration_form.submit.data == True:

            entered_email = request.form.get('email')
            new_user_obj = db.session.execute(db.select(User).where(User.email == entered_email)).scalar()

            if new_user_obj:
                flash("You've have already signed up with that email, log in Instead!")
                return redirect("login")

            else:
                hashed_salted_pwd = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256',
                                                           salt_length=8)

                new_user = User(
                    email=request.form.get("email"),
                    name=request.form.get("username"),
                    password=hashed_salted_pwd
                )
                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)  # Log in and authenticate user after adding details to database.
                return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=registration_form)


#  Retrieving a user from the database based on their email and authenticating them that they are registered user or not..
@app.route('/login', methods=['GET', 'POST'])
def login():
    """this route renders login page and in post request do authentication and that user provided correct email or password or not."""

    loginform = LoginForm()
    if loginform.validate_on_submit() and loginform.submit.data == True:
        email = request.form.get('email')
        password = request.form.get('password')
        user_obj = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if not user_obj:  # Handle non-existent email_id
            flash("That Email, does not exist. Please try again!")
            return redirect("login")

        else:  # if email_id exist.
            pwd_hash = user_obj.password

            if check_password_hash(pwd_hash, password):  # it will check the stored hash password with plain text password using this method and return True if correct password provided.
                login_user(user_obj)
                return redirect(url_for("get_all_posts"))

            else:
                flash("Password Incorrect. Please try again!")
                return redirect(url_for("login"))

    return render_template("login.html", loginform=loginform)


@app.route('/logout')
def logout():
    """this route is responsible for rendering the all blog posts in the home page by logging out a user."""

    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    """this route is responsible for rendering the all blog posts in the home page."""

    create_database()

    blog_obj = read_blogs_data()
    posts = [blog for blog in blog_obj]

    return render_template("index.html", all_posts=posts)


# Allowing only logged-in users to comment on posts
@app.route('/show_post/<int:post_id>', methods = ['GET', 'POST'])
def show_post(post_id):
    """this route is responsible for rendering the blog on which user has clicked on it."""

    requested_blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    comment_form = CommentForm()
    if request.method == 'POST' and comment_form.validate_on_submit() and comment_form.submit.data == True:

            if current_user.is_authenticated:

                new_comment = Comment(
                    comment_author=current_user,
                    parent_post=requested_blog_post,
                    text=request.form.get("comment"),
                )

                db.session.add(new_comment)
                db.session.commit()
                print("new comment added in the database successfully")
                return redirect(url_for("show_post", post_id = post_id))

            else:
                flash("You need to login or register to comment!")
                return redirect(url_for("login"))

    new_comments = requested_blog_post.comments
    return render_template("post.html", post=requested_blog_post, form = comment_form, comments = new_comments)


#Used a decorator so only an admin user can edit a post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    """this route is responsible for creating a new blog post in the blog website."""

    form = BlogForm()

    # here it will render the home page with the new post added in the database and also renders that new post in the home page.
    if request.method == "POST":

        if form.validate_on_submit() and form.submit.data == True:
            dt = date.today()
            current_date = dt.strftime("%A %d, %Y")

            new_blog = BlogPost(
                title=request.form.get("title"),
                subtitle=request.form.get("subtitle"),
                img_url=request.form.get("img_url"),
                body=request.form.get("body"),
                date=current_date,
                author_id= current_user.id,
            )

            db.session.add(new_blog)
            db.session.commit()
            print("new blog added in the database successfully")

            return redirect(url_for('get_all_posts'))

    # here it will render the mak-post page
    return render_template("make-post.html", form=form)


#Used a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    """this route is responsible for rendering the blog post which we want to edit with pre populate all the things and update the blog post when user clicks on submit button."""

    blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    if request.method == 'POST':  # this will render the show post page with the updated blog post details.

        blog_post.title = request.form['title']
        blog_post.subtitle = request.form['subtitle']
        blog_post.img_url = request.form['img_url']
        blog_post.author = current_user
        blog_post.body = request.form['body']

        db.session.commit()

        print("Edited blog details successfully updated in the database")
        return redirect(url_for('show_post', post_id=blog_post.id))

    edit_form = BlogForm(
        title=blog_post.title,
        subtitle=blog_post.subtitle,
        img_url=blog_post.img_url,
        author=blog_post.author,
        body=blog_post.body,
    )

    return render_template("make-post.html", id=post_id, form=edit_form)


#  Using a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    """this route is responsible for deleting the blog post when user clicks on the X in the blog post."""

    blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(blog_post)
    db.session.commit()

    print("The requested blog post is being successfully deleted.")
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    """this route is responsible for rendering the about page."""

    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """this route is responsible for rendering the contact page."""

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_no = request.form['phone']
        message = request.form['message']

        message_data = f'Name: {name}\nEmail: {email}\nPhone_no: {phone_no}\nMessage: {message}'

        send_mail(message_data)

        msg = "successful"
        return render_template("contact.html",
                               successful_msg=msg)  # once the message sent successful this will render contact.html page and show succesful sent message

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
